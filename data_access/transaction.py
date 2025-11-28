import sqlite3
from settings import CONNECTION_DATABASE


class Transaction:
    def __enter__(self):
        self.conn = sqlite3.connect(CONNECTION_DATABASE)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        self.cur.execute("BEGIN;")
        return self.cur

    def __exit__(self, exc_type, exc_val, _):
        if exc_type is None:
            self.conn.commit()
        else:
            print(f"[Transaction][Error] {exc_type.__name__}: {exc_val}")
            self.conn.rollback()
        self.conn.close()
