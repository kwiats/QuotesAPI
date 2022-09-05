import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS quotes (
id INTEGER PRIMARY KEY,
id_quote INTEGER,
quote TEXT,
origin TEXT,
authorId INTEGER,
FOREIGN KEY(authorId) REFERENCES authors(id))
"""


cursor.execute(CREATE_TABLE)

CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS authors (
id INTEGER PRIMARY KEY,
author TEXT)
"""


cursor.execute(CREATE_TABLE)

conn.commit()
conn.close()
