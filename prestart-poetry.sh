#! /usr/bin/env bash

# Uncomment if you don't want poetry to create a virtual environment for you
# poetry config virtualenvs.create false

# Install dependencies
poetry install --no-root
# To skip development dependencies use this line instead
# poetry install --no-root --no-dev

# Run migrations
alembic upgrade head

# Create initial data
python init_db.py