# Makefile for Order Management System

.PHONY: help run test lint format migrate-up migrate-down clean seed

help:
	@echo "Available commands:"
	@echo "  run           - Run the FastAPI application"
	@echo "  test          - Run all tests using pytest"
	@echo "  test-unit     - Run unit tests"
	@echo "  lint          - Run ruff for linting"
	@echo "  format        - Run ruff for formatting"
	@echo "  migrate-up    - Run alembic migrations"
	@echo "  migrate-down  - Rollback last alembic migration"
	@echo "  seed          - Seed the database with sample products"
	@echo "  clean         - Remove cache and temporary files"

run:
	uv run python src/main.py

test:
	uv run pytest tests/unit/ tests/integration/ -v

test-unit:
	uv run pytest tests/unit/ -v

lint:
	uv run ruff check .

format:
	uv run ruff format .

migrate-up:
	uv run alembic upgrade head

migrate-down:
	uv run alembic downgrade -1

seed:
	uv run python seed/seed_products.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
