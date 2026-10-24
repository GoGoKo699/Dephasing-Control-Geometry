#!/usr/bin/env python3
"""Run the focused verification suite against stored analytic expectations."""

from __future__ import annotations

import argparse
import json
import math
import platform
from pathlib import Path
import sys

import numpy as np
import scipy

from cases import evaluate_all


def compare(actual, expected, path, absolute, relative, failures):
    if isinstance(expected, dict):
        if not isinstance(actual, dict) or actual.keys() != expected.keys():
            failures.append(f"{path}: object keys differ")
            return 0
        return sum(
            compare(actual[key], value, f"{path}.{key}", absolute, relative, failures)
            for key, value in expected.items()
        )
    if isinstance(expected, list):
        if not isinstance(actual, list) or len(actual) != len(expected):
            failures.append(f"{path}: list lengths differ")
            return 0
        return sum(
            compare(value, reference, f"{path}[{index}]", absolute, relative, failures)
            for index, (value, reference) in enumerate(zip(actual, expected))
        )
    if isinstance(expected, (int, float)):
        if not math.isclose(float(actual), float(expected), rel_tol=relative, abs_tol=absolute):
            failures.append(f"{path}: observed {actual!r}, expected {expected!r}")
        return 1
    if actual != expected:
        failures.append(f"{path}: observed {actual!r}, expected {expected!r}")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optionally write the full observed JSON report.")
    arguments = parser.parse_args()
    reference_path = Path(__file__).with_name("expected_results.json")
    reference = json.loads(reference_path.read_text(encoding="utf-8"))
    observed = evaluate_all()
    failures = []
    checks = compare(
        observed,
        reference["values"],
        "results",
        reference["tolerances"]["absolute"],
        reference["tolerances"]["relative"],
        failures,
    )
    report = {
        "schema_version": 1,
        "passed": not failures,
        "numerical_comparisons": checks,
        "runtime": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
        },
        "failures": failures,
        "values": observed,
    }
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    if failures:
        for failure in failures:
            print(f"FAIL {failure}", file=sys.stderr)
        return 1
    print(f"PASS: {len(observed)} verification families, {checks} numerical comparisons.")
    print("Checked graph/product, logical Choi weights, controlled-gate resources, and continuous one-jump correction.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
