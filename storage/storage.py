import sqlite3

def init_db():
    conn = sqlite3.connect('favorites.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS favorites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            character_id INTEGER NOT NULL,
            character_name TEXT NOT NULL,
            character_image TEXT NOT NULL,
            comment TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def add_favorite(user_id, character_id, character_name, character_image, comment):
    conn = sqlite3.connect('favorites.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO favorites (user_id, character_id, character_name, character_image, comment)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, character_id, character_name, character_image, comment))
    conn.commit()
    conn.close()

def get_favorites(user_id):
    conn = sqlite3.connect('favorites.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT character_name, character_image, comment 
        FROM favorites 
        WHERE user_id = ?
        ORDER BY timestamp DESC
    ''', (user_id,))
    favorites = cursor.fetchall()
    conn.close()
    return favorites
