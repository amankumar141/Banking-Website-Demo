import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS bank_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT NOT NULL,
        details TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

print("Database initialized successfully.")