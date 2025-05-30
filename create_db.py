import sqlite3

conn = sqlite3.connect('ev_predictions.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    port INTEGER NOT NULL,
    lat REAL NOT NULL,
    lon REAL NOT NULL,
    duration INTEGER NOT NULL,
    charging INTEGER NOT NULL,
    predicted_energy REAL NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
conn.close()

print("Database and table created successfully!")
