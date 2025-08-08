import argparse
import string
import secrets
from typing import Callable


def positive_int(value: str) -> int:
    parsed_value = int(value)
    if parsed_value < 1:
        raise argparse.ArgumentTypeError("value must be >= 1")
    return parsed_value


def build_character_pool(include_symbols: bool, include_numbers: bool) -> str:
    characters = string.ascii_letters
    if include_symbols:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits
    return characters


def generate_password(length: int, character_pool: str, chooser: Callable[[str], str]) -> str:
    return "".join(chooser(character_pool) for _ in range(length))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create strong passwords using a simple string builder"
    )
    parser.add_argument(
        "-l",
        "--length",
        help="Length of each generated password",
        type=positive_int,
        default=8,
    )
    parser.add_argument(
        "-g",
        "--count",
        help="Number of passwords to generate",
        type=positive_int,
        default=1,
    )
    parser.add_argument(
        "-s",
        "--symbols",
        help="Include symbols (punctuation)",
        action="store_true",
    )
    parser.add_argument(
        "-n",
        "--numbers",
        help="Include numbers (0-9)",
        action="store_true",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    character_pool = build_character_pool(args.symbols, args.numbers)
    chooser = secrets.choice  # cryptographically secure selection

    for _ in range(args.count):
        print(generate_password(args.length, character_pool, chooser))


if __name__ == "__main__":
    main()
