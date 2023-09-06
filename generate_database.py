#!/usr/bin/env python3
import sqlite3


db_file = "targets.db"

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

create_table_sql = """
CREATE TABLE IF NOT EXISTS Targets (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    IP TEXT NOT NULL,
    MAC TEXT NOT NULL,
    LAT TEXT NOT NULL,
    lng TEXT NOT NULL,
    DEVICE TEXT NOT NULL
);
"""

cursor.execute(create_table_sql)

conn.commit()
conn.close()

print("Database created successfully.")
