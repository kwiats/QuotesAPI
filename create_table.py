import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS quotes (
id INTEGER PRIMARY KEY,
id_quote INTEGER,
quote TEXT,
author TEXT,
origin TEXT)
"""


cursor.execute(CREATE_TABLE)

conn.commit()
conn.close()
