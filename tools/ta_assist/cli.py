"""CLI entry: check / prompt / scan / prepare / index."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .checker import format_report, run_checks, summarize
from .indexer import regenerate
from .promptgen import PROMPT_TYPES, generate_prompt, suggest_next
from .scanner import scan_bootstrap, scan_native
from .util import is_native, repo_root


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="ta-assist",
        description=(
            "technology-audit assist: structure check, prompt prep, and index generation. "
            "Does not invent Sheet/Application content — only regenerates catalogs from Sheet YAML."
        ),
    )
    parser.add_argument("--version", action="version", version=f"ta-assist {__version__}")
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="path to technology-audit repo (default: discover from cwd)",
    )

    sub = parser.add_subparsers(dest="cmd", required=True)

    p_scan = sub.add_parser("scan", help="print repository scan / status")
    p_scan.add_argument("path", nargs="?", default=None, help="native root or foreign path/URL")

    p_check = sub.add_parser("check", help="structure and consistency checks")
    p_check.add_argument(
        "--format",
        choices=("text", "github"),
        default="text",
        help="report format",
    )

    p_prompt = sub.add_parser("prompt", help="generate a prompt pack into artifacts/prompts/")
    p_prompt.add_argument(
        "type",
        choices=sorted(PROMPT_TYPES) + ["next"],
        help="prompt type (next = next-step)",
    )
    p_prompt.add_argument("--project", default="", help="project_id")
    p_prompt.add_argument("--slug", default="", help="tech slug")
    p_prompt.add_argument("--audit", default="", help="audit campaign id")
    p_prompt.add_argument(
        "--repo",
        default="",
        help="source repo URL/path for bootstrap-repo",
    )
    p_prompt.add_argument(
        "--stdout",
        action="store_true",
        help="also print prompt body",
    )
    p_prompt.add_argument(
        "--dry-run",
        action="store_true",
        help="do not write artifact file",
    )

    p_prep = sub.add_parser(
        "prepare",
        help="simple UX: prepare next | prepare bootstrap <url>",
    )
    p_prep.add_argument(
        "action",
        choices=("next", "bootstrap", "check"),
        help="next step / bootstrap foreign repo / run check",
    )
    p_prep.add_argument("repo", nargs="?", default="", help="URL/path for bootstrap")
    p_prep.add_argument("--project", default="")
    p_prep.add_argument("--stdout", action="store_true")

    sub.add_parser(
        "index",
        help="regenerate technologies/index.yaml + README.md from Sheet YAML",
    )

    args = parser.parse_args(argv)
    root = repo_root(args.root) if args.root else repo_root()

    if args.cmd == "scan":
        return cmd_scan(root, args.path)
    if args.cmd == "check":
        return cmd_check(root, args.format)
    if args.cmd == "index":
        return cmd_index(root)
    if args.cmd == "prompt":
        ptype = "next-step" if args.type == "next" else args.type
        return cmd_prompt(
            root,
            ptype,
            project=args.project,
            slug=args.slug,
            audit=args.audit,
            repo=args.repo,
            stdout=args.stdout,
            dry_run=args.dry_run,
        )
    if args.cmd == "prepare":
        if args.action == "check":
            return cmd_check(root, "text")
        if args.action == "bootstrap":
            if not args.repo:
                print("prepare bootstrap requires a repo URL or path", file=sys.stderr)
                return 2
            return cmd_prompt(
                root,
                "bootstrap-repo",
                project=args.project,
                repo=args.repo,
                stdout=args.stdout,
                dry_run=False,
            )
        if args.action == "next":
            return cmd_prompt(
                root,
                "next-step",
                project=args.project,
                stdout=args.stdout,
                dry_run=False,
            )
    return 2


def cmd_scan(root: Path, path: str | None) -> int:
    if path and (path.startswith("http") or path.startswith("git@") or not is_native(Path(path) if Path(path).exists() else root)):
        if path.startswith("http") or path.startswith("git@"):
            result = scan_bootstrap(path)
        elif Path(path).exists() and not is_native(Path(path)):
            result = scan_bootstrap(path)
        else:
            target = repo_root(Path(path)) if path else root
            result = scan_native(target)
    else:
        target = repo_root(Path(path)) if path else root
        if is_native(target):
            result = scan_native(target)
        else:
            result = scan_bootstrap(str(path or target))
    print(result.status_text())
    if result.native:
        typ, params = suggest_next(result)
        print(f"\nsuggested_next_prompt: {typ}")
        for k, v in params.items():
            print(f"  {k}: {v}")
    return 0


def cmd_index(root: Path) -> int:
    info = regenerate(root)
    print(
        f"index: {info['sheet_count']} sheets → {info['index_yaml']} + {info['readme']}; "
        f"{info['project_count']} projects → {info['projects_index']} + {info['projects_readme']} "
        f"(planned={info['planned']}, sheet_errors={info.get('sheet_errors', 0)})"
    )
    return 1 if info.get("sheet_errors") else 0


def cmd_check(root: Path, fmt: str) -> int:
    findings = run_checks(root)
    report = format_report(findings)
    print(report)
    if fmt == "github":
        gh = Path(os_environ_github_step_summary())
        if gh:
            try:
                with gh.open("a", encoding="utf-8") as f:
                    f.write(report)
                    f.write("\n")
            except OSError:
                pass
    e, _, _ = summarize(findings)
    return 1 if e else 0


def os_environ_github_step_summary() -> str:
    import os

    return os.environ.get("GITHUB_STEP_SUMMARY", "")


def cmd_prompt(
    root: Path,
    prompt_type: str,
    *,
    project: str = "",
    slug: str = "",
    audit: str = "",
    repo: str = "",
    stdout: bool = False,
    dry_run: bool = False,
) -> int:
    try:
        path, body = generate_prompt(
            prompt_type,
            root=root,
            project_id=project,
            slug=slug,
            audit_id=audit,
            source_repo=repo,
            write=not dry_run,
        )
    except (ValueError, FileNotFoundError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if path:
        print(f"wrote {path}")
    if stdout or dry_run:
        print(body)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
