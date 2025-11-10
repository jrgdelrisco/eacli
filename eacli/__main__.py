"""Command-line entry for eacli."""

import argparse
import sys

from . import __version__


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(prog="eacli", description="eacli console application")
    parser.add_argument("--version", action="store_true", help="Show version")
    args = parser.parse_args(argv)

    if args.version:
        print(f"eacli {__version__}")
    else:
        print("Hello from eacli — your console app is ready!")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
