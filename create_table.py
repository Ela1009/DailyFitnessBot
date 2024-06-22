import sqlite3

conn = sqlite3.connect('fitness_bot.db')
cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    phone_number TEXT NOT NULL,
    preferred_time TEXT NOT NULL,
    workout_preference TEXT,
    tip_preference TEXT,
    last_sent TIMESTAMP
);
'''

cursor.execute(create_table_query)

conn.commit()
conn.close()

print("Table created successfully.")
