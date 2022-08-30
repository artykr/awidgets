#! /usr/bin/env bash

# Install dependencies
pip install -r requirements.txt

# Run migrations
alembic upgrade head

# Create initial data
python init_db.py