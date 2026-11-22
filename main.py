from __future__ import annotations
import argparse
import re
from dataclasses import dataclass

@dataclass(frozen=True)
class RefSpec:
    source: str
    destination: str
    force: bool = False
    negative: bool = False
    deletion: bool = False

def parse_refspec(value: str) -> RefSpec:
    if not value:
        raise ValueError("Refspec cannot be empty")
    if value.startswith("^"):
        pattern = value[1:]
        if not pattern or ":" in pattern or pattern.count("*") > 1:
            raise ValueError("Invalid negative refspec")
        return RefSpec(pattern, "", negative=True)
    force = value.startswith("+")
    body = value[1:] if force else value
    if ":" not in body:
        raise ValueError("Positive refspecs must contain ':' in this explainer")
    source, destination = body.split(":", 1)
    if not destination:
        raise ValueError("Destination ref cannot be empty")
    if source == "":
        if "*" in destination:
            raise ValueError("Deletion refspec cannot contain a wildcard")
        return RefSpec("", destination, force=force, deletion=True)
    if source.count("*") > 1 or destination.count("*") > 1:
        raise ValueError("At most one wildcard is supported on each side")
    if source.count("*") != destination.count("*"):
        raise ValueError("Source and destination must either both contain '*' or neither")
    return RefSpec(source, destination, force=force)

def match(pattern: str, value: str) -> str | None:
    if "*" not in pattern:
        return "" if pattern == value else None
    before, after = pattern.split("*", 1)
    if not value.startswith(before) or not value.endswith(after):
        return None
    middle = value[len(before):len(value) - len(after) if after else None]
    return middle if middle else None

def explain(refspecs: list[str], refs: list[str]) -> list[str]:
    parsed = [parse_refspec(item) for item in refspecs]
    negatives = [item for item in parsed if item.negative]
    positives = [item for item in parsed if not item.negative]
    excluded = {ref for ref in refs if any(match(rule.source, ref) is not None for rule in negatives)}
    lines: list[str] = []
    for rule in positives:
        if rule.deletion:
            lines.append(f"DELETE {rule.destination} (destination removal; no source ref)")
            continue
        for ref in refs:
            capture = match(rule.source, ref)
            if capture is None or ref in excluded:
                continue
            destination = rule.destination.replace("*", capture)
            marker = "FORCE " if rule.force else ""
            lines.append(f"{marker}{ref} -> {destination}")
    return lines

def main() -> int:
    parser = argparse.ArgumentParser(description="Explain Git refspec mappings without running Git.")
    parser.add_argument("--refspec", action="append", required=True, help="Refspec; repeat for multiple rules")
    parser.add_argument("--refs", default="refs/heads/main,refs/heads/dev,refs/tags/v1.0.0",
                        help="Comma-separated source refs to simulate")
    args = parser.parse_args()
    try:
        lines = explain(args.refspec, [part.strip() for part in args.refs.split(",") if part.strip()])
    except ValueError as exc:
        parser.error(str(exc))
    print("\n".join(lines) if lines else "No refs matched the supplied refspecs.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
