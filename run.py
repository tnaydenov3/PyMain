import sys

from solutions.command import CommandCall


def main() -> None:
    args = sys.argv

    if args:
        CommandCall.call(*args)


if __name__ == "__main__":
    main()
