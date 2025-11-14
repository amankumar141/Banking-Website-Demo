import sqlite3

# Connect to the database
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Try to fetch all rows from the bank_data table
try:
    c.execute("SELECT * FROM bank_data")
    rows = c.fetchall()
    print("✅ Data in bank_data table:")
    for row in rows:
        print(row)
except sqlite3.OperationalError as e:
    print("❌ Error:", e)

conn.close()