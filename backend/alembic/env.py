# alembic/env.py
import sys
import os
from sqlalchemy import engine_from_config, pool
from alembic import context
from sqlmodel import SQLModel
from app.core.database import settings

# Add the app directory to the Python path so Alembic can find the models
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

# This is your metadata, Alembic will use this for autogenerating migrations
target_metadata = SQLModel.metadata

def run_migrations_online():
    # Get the database URL from settings, remove any extra characters like +asyncpg
    connectable = engine_from_config({"sqlalchemy.url": settings.DATABASE_URL.replace("+asyncpg", "")},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool, 
    )

    # Connect to the database
    with connectable.connect() as connection:
        # Configure Alembic to use the connection and target metadata (for migrations)
        context.configure(connection=connection, target_metadata=target_metadata)
        # Start the transaction and run migrations
        with context.begin_transaction():
            context.run_migrations()


# This will run the migrations in 'online' mode
run_migrations_online()
