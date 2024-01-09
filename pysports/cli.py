"""Console script for pysports."""

import fire


def help() -> None:
    print("pysports")
    print("=" * len("pysports"))
    print("Python API for Sports Data")


def main() -> None:
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
