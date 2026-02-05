# copier-minimal-python

[![CI](https://github.com/jooh/copier-minimal-python/actions/workflows/ci.yml/badge.svg)](https://github.com/jooh/copier-minimal-python/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](template/LICENSE)

A minimal [copier](https://copier.readthedocs.io/) template for Python projects with uv, pytest, ruff, and optional CLI support.

## Features

- [uv](https://docs.astral.sh/uv/) for dependency management
- [pytest](https://docs.pytest.org/) for testing
- [ruff](https://docs.astral.sh/ruff/) for linting and formatting
- [pyright](https://github.com/microsoft/pyright) for type checking
- Optional [Typer](https://typer.tiangolo.com/) CLI
- GitHub Actions CI/CD workflows
- MIT license

## Usage

```bash
uvx copier copy gh:jooh/copier-minimal-python my-project
```

Or with copier installed:

```bash
copier copy gh:jooh/copier-minimal-python my-project
```

## Template options

| Option | Description | Default |
|--------|-------------|---------|
| `project_name` | Project name (kebab-case) | - |
| `package_name` | Python package name (snake_case) | derived from project_name |
| `description` | One-line project description | - |
| `min_python_version` | Minimum Python version | 3.12 |
| `has_cli` | Include Typer CLI | true |
| `author_name` | Author name | - |
| `repo_owner` | GitHub username/org | - |

## Development

```bash
make test
```

See [AGENTS.md](AGENTS.md) for more details on the template structure.
