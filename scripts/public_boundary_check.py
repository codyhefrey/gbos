"""Check tracked public files for paths/secrets that cannot be deliberately released.

This is defense in depth, not a DLP certification or a grant/restriction of
the Apache-2.0 license. Public Git history may already have been copied.
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROHIBITED_SEGMENTS = {
    "private", "proprietary", "confidential", "internal-only",
    "secrets", "credentials", "customer-exports", "production-dumps",
}
PROHIBITED_NAMES = {
    ".env", "id_rsa", "id_ed25519", "service-account.json",
    "private.key", "production.db", "customers.csv",
}
BLOCKED_SUFFIXES = (".pem", ".p12", ".pfx", ".key", ".sqlite", ".sqlite3")
# Exclude this source file from content patterns, since it defines the patterns.
SKIP_CONTENT = {"scripts/public_boundary_check.py", "LICENSE"}
SECRET_PATTERNS = [
    re.compile(r"-{5}BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-{5}"),
    re.compile(r"\b(?:ghp_|gho_|ghu_|ghs_)[A-Za-z0-9]{30,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-proj-[A-Za-z0-9_-]{20,}\b"),
]


def check() -> list[str]:
    tracked = subprocess.check_output(
        ["git", "-C", str(ROOT), "ls-files", "-z"],
        stderr=subprocess.DEVNULL,
    )
    problems: list[str] = []
    for raw in tracked.split(b"\0"):
        if not raw:
            continue
        relative = raw.decode("utf-8", errors="replace")
        p = pathlib.PurePosixPath(relative)
        if (
            any(seg.lower() in PROHIBITED_SEGMENTS for seg in p.parts)
            or p.name.lower() in PROHIBITED_NAMES
            or p.name.lower().endswith(BLOCKED_SUFFIXES)
            or p.name.lower().startswith(".env.")
        ):
            problems.append(f"Blocked public asset path: {relative}")
            continue
        if relative in SKIP_CONTENT:
            continue
        file = ROOT.joinpath(*p.parts)
        if file.is_symlink():
            problems.append(f"Public symlink needs manual review: {relative}")
            continue
        if not file.is_file() or file.stat().st_size > 1024 * 1024:
            continue
        try:
            body = file.read_text(encoding="utf-8")
        except UnicodeError:
            continue
        if any(pattern.search(body) for pattern in SECRET_PATTERNS):
            # Do not print possible leaked secrets, only the filename.
            problems.append(f"Possible credential in public file: {relative}")
    return problems


if __name__ == "__main__":
    errors = check()
    if errors:
        for issue in errors:
            print(issue, file=sys.stderr)
        print("BLOCKED: remove sensitive materials from this public change.", file=sys.stderr)
        raise SystemExit(1)
    print("PASS: no prohibited public paths or obvious credentials detected.")
