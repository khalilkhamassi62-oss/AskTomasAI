import sqlite3

from backend.db.migration_runner import run_migrations, BASE_TABLES


def test_base_tables_created():
    # Run migrations against an in‑memory SQLite DB
    conn = run_migrations()
    cursor = conn.cursor()
    for table in BASE_TABLES:
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table,)
        )
        result = cursor.fetchone()
        assert result is not None, f"Table '{table}' was not created by migrations"
    conn.close()
