# lumpo_stdlib/db.py
import sqlite3

class SQLiteDB:
    def __init__(self, path=":memory:"):
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row

    def execute(self, sql, params=None):
        cur = self.conn.cursor()
        if params is None:
            cur.execute(sql)
        else:
            cur.execute(sql, params)
        self.conn.commit()
        return cur.lastrowid

    def query(self, sql, params=None):
        cur = self.conn.cursor()
        if params is None:
            cur.execute(sql)
        else:
            cur.execute(sql, params)
        rows = cur.fetchall()
        return [dict(row) for row in rows]

    def close(self):
        self.conn.close()

def open(path=":memory:"):
    return SQLiteDB(path)
