#!/usr/bin/env python3

import argparse

from lib.semantic_search import (
    embed_text, 
    verify_embeddings, 
    verify_model,
    embed_query_text,
    SemanticSearch,
)
from lib.search_utils import load_movies


def main() -> None:
    parser = argparse.ArgumentParser(description="Semantic Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("verify", help="Verify that the embedding model is loaded")

    single_embed_parser = subparsers.add_parser(
        "embed_text", help="Generate an embedding for a single text"
    )
    single_embed_parser.add_argument("text", type=str, help="Text to embed")

    subparsers.add_parser(
        "verify_embeddings", help="Verify embeddings for the movie dataset"
    )

    single_embed_parser = subparsers.add_parser(
        "embedquery", help="Generate an embedding for a query text"
    )
    single_embed_parser.add_argument("query", type=str, help="Query text to embed")

    single_embed_parser = subparsers.add_parser(
        "search", help="Search through documents using provided query"
    )
    single_embed_parser.add_argument("query", type=str, help="Query text for search")
    single_embed_parser.add_argument("--limit", type=int, default=5, help="Limit for the number of search results returned")

    args = parser.parse_args()

    match args.command:
        case "verify":
            verify_model()
        case "embed_text":
            embed_text(args.text)
        case "verify_embeddings":
            verify_embeddings()
        case "embedquery":
            embed_query_text(args.query)
        case "search":
            sem_search = SemanticSearch()
            sem_search.load_or_create_embeddings(load_movies())
            results = sem_search.search(args.query, args.limit)
            for i in range(0, len(results)):
                print(f"{i+1}. {results[i]["title"]} (score: {results[i]["score"]})")
                print(f"{results[i]["description"][:100]} ...")
                print("")
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
