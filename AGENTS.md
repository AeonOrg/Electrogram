# Agent Instructions

This document provides instructions for AI agents working on this codebase.

## Dependency Management

- Use `uv` instead of `pip` for installing and managing Python packages.

## Code Style and Quality for big changes in python code files

- Before submitting any changes, always run the following commands from the root of the repository:
  - `ruff check . --fix`: This will check for linting errors and automatically fix many of them.
  - `ruff format .`: This will format the code according to the project's style guide.
  - `uv ty check`: This will check type annotations. after type check must fix at least some type errors

## Update this AGENTS.md if any suggestions should be applied in future.
