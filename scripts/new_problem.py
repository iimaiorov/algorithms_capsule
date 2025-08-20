#!/usr/bin/env python3
"""Utility to scaffold a new algorithm problem."""

from __future__ import annotations

import argparse
from pathlib import Path

CATEGORIES = ["arrays", "strings", "hashing", "sliding_window", "dp"]

TASK_TEMPLATE = "# {title}\n\nTODO: describe the problem.\n"
SOLUTION_TEMPLATE = (
    "from typing import Any\n\n"
    "def {func}(data: Any) -> Any:\n"
    '    """TODO: implement solution"""\n'
    "    raise NotImplementedError\n"
)
TESTS_TEMPLATE = (
    "import pytest\n\n"
    "from .solution import {func}\n\n"
    "def test_example() -> None:\n"
    "    assert {func}(...) == ...\n"
)
EXPLANATION_TEMPLATE = "# Explanation\n\nTODO: describe the idea and complexity.\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new problem stub")
    parser.add_argument("category", choices=CATEGORIES, help="Problem category")
    parser.add_argument("problem", help="Problem name in snake_case")
    args = parser.parse_args()

    base = Path(__file__).resolve().parents[1]
    problem_dir = base / "algorithms" / args.category / args.problem
    if problem_dir.exists():
        raise SystemExit(f"{problem_dir} already exists")

    problem_dir.mkdir(parents=True)
    (problem_dir / "__init__.py").touch()
    (problem_dir / "task.md").write_text(
        TASK_TEMPLATE.format(title=args.problem.replace("_", " ").title())
    )
    (problem_dir / "solution.py").write_text(
        SOLUTION_TEMPLATE.format(func=args.problem)
    )
    (problem_dir / f"tests{args.problem}.py").write_text(TESTS_TEMPLATE.format(func=args.problem))
    (problem_dir / "explanation.md").write_text(EXPLANATION_TEMPLATE)
    print(f"Created {problem_dir}")


if __name__ == "__main__":
    main()
