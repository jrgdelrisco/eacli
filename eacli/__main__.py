"""Command-line entry for eacli."""

import argparse
import sys

from . import __version__
from .config_loader import get_enabled_apps


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(prog="eacli", description="eacli console application")
    parser.add_argument("--version", action="store_true", help="Show version")
    parser.add_argument("--show-apps", action="store_true", help="Show enabled apps")
    args = parser.parse_args(argv)

    if args.version:
        print(f"eacli {__version__}")
    elif args.show_apps:
        enabled_apps = get_enabled_apps()
        if enabled_apps:
            print("Enabled apps:")
            for app in enabled_apps:
                print(f"  - {app['name']}: {app['description']}")
        else:
            print("No enabled apps found.")
    else:
        print("Hello from eacli — your console app is ready!")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
