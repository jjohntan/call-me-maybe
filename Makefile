# Syncing the environment manually is especially useful for ensuring editor has the correct versions of dependencies.
install:
	uv sync

run:
	uv run python -m src

debug: 
	uv run python -m pdb src

# First finds all __pycache__ folders in current directory.
# Execute rm -r {} + to delete each folder at step above ({} signify for placeholder and + to end the command).
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +

# check code syntax and provide instructions on how to clean it
lint:
	uv run flake8 src
	uv run mypy src --warn-return-any \
	--warn-unused-ignores \
	--ignore-missing-imports \
	--disallow-untyped-defs \
	--check-untyped-defs

lint-strict:
	uv run flake8 src
	uv run mypy --strict src

# prevent same name target and file conflict
.PHONY: install run debug clean lint lint-strict

# uv: An extremely fast Python package and project manager, written in Rust.