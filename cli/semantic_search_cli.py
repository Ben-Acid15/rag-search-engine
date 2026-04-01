#!/usr/bin/env python3

import argparse

from lib.semantic_search import (
    verify_model,
    embed_text
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Semantic Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("verify", help="Verify that the embedding model is loaded")

    embed_parser = subparsers.add_parser("embed_text", help="Embed the given text")
    embed_parser.add_argument("text", type=str, help="Text that is meant to be embedded")

    args = parser.parse_args()

    match args.command:
        case "verify":
            verify_model()
        case "embed_text":
            embed_text(args.text)
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
