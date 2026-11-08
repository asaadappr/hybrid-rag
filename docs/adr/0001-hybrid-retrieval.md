# ADR 0001: Hybrid retrieval with three lanes and a reranker

- Status: Accepted
- Date: 2026-11-09

## Context
RAG system, with exact order number matching and semantic matching capabilities

## Decision
Exact match for order numbers, BM25 always, semantic always, then merge,
rerank, and generate with Claude.

## Alternatives considered
- Semantic search only: will miss the exact matches
- BM25 only: for searches which require semantic search, this will fail.
- BM25 for order numbers instead of exact match: will be thinking about this

## Consequences
- Good: addressed later
- Costs: yet to be computed
