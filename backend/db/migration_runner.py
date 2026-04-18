import sqlite3
import pathlib
from typing import List

MIGRATIONS_DIR = pathlib.Path(__file__).parent / 'migrations'

def _load_sql_files() -> List[pathlib.Path]:
    """Return a sorted list of *.sql migration files.
    Raises FileNotFoundError if the migrations directory does not exist.
    """
    if not MIGRATIONS_DIR.is_dir():
        raise FileNotFoundError(f"Migrations directory {MIGRATIONS_DIR} not found")
    return sorted(MIGRATIONS_DIR.glob('*.sql'))

def _apply_sql(conn: sqlite3.Connection, sql_path: pathlib.Path) -> None:
    """Execute the SQL script at *sql_path* on the given connection."""
    conn.executescript(sql_path.read_text(encoding='utf-8'))

def run_migrations(db_path: str = ':memory:') -> sqlite3.Connection:
    """Run all migrations against the SQLite database at *db_path*.
    Returns the ``sqlite3.Connection`` after applying migrations.
    """
    conn = sqlite3.connect(db_path)
    try:
        for sql_file in _load_sql_files():
            _apply_sql(conn, sql_file)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    return conn

# List of tables created by the base migration – used in tests.
BASE_TABLES = [
    'companies',
    'users',
    'agents',
    'sessions',
    'messages',
    'approvals',
]
