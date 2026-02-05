# Agent guide for copier-minimal-python

This is a copier template for Python projects. It generates new Python projects with uv, pytest, ruff, and optional CLI support.

## Repository structure

- `copier.yml` - Template configuration and questions
- `template/` - Template files that get copied to new projects (uses Jinja2 templating)
- `tests/` - Integration tests for the template itself
- `Makefile` - Development commands for the template repo

## Development

- Run `make test` to verify the template generates correctly
- The test creates a temporary project using copier with default values and checks basic structure

## How the template works

- `_subdirectory: template` in copier.yml tells copier to source files from `template/`
- `_templates_suffix: ""` means all files are templates (no `.jinja` extension needed)
- Template variables like `{{ project_name }}` are replaced during generation
- Conditional blocks like `{% if has_cli %}` control optional features

## Making changes

1. Edit files in `template/` to change what gets generated
2. Edit `copier.yml` to add/modify template questions
3. Run `make test` to verify changes work
