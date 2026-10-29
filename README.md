# expnote

Python library for documenting experiments and generating HTML research reports.

## Development

Install the development environment:

    uv sync

Run quality checks:

    uv run ruff check .
    uv run ruff format --check .
    uv run basedpyright
    uv run pytest
