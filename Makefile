.PHONY: help install dev test lint format clean docker-up docker-down

help:
	@echo "Token AI Ecosystem - Development Commands"
	@echo "==========================================="
	@echo "make install       - Install dependencies"
	@echo "make dev           - Run development server"
	@echo "make test          - Run tests"
	@echo "make lint          - Run linters"
	@echo "make format        - Format code"
	@echo "make clean         - Clean up artifacts"
	@echo "make docker-up     - Start Docker services"
	@echo "make docker-down   - Stop Docker services"
	@echo "make db-migrate    - Run database migrations"

.DEFAULT_GOAL := help

install:
	@echo "Installing Python dependencies..."
	pip install -r requirements.txt
	@echo "Installing Node dependencies..."
	npm install

dev:
	@echo "Starting development server..."
	uvicorn main:app --reload --host 0.0.0.0 --port 8000

test:
	@echo "Running tests..."
	pytest -v --cov=src tests/

lint:
	@echo "Running linters..."
	flake8 src/ tests/
	mypy src/
	pylint src/

format:
	@echo "Formatting code..."
	black src/ tests/
	isort src/ tests/

clean:
	@echo "Cleaning up..."
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".coverage" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/ *.egg-info

docker-up:
	@echo "Starting Docker services..."
	docker-compose up -d

docker-down:
	@echo "Stopping Docker services..."
	docker-compose down

db-migrate:
	@echo "Running database migrations..."
	alembic upgrade head
