import sqlite3

def init_db():
    conn = sqlite3.connect("app.db")
    c = conn.cursor()

    # Users table
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    # Results table
    c.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            image_name TEXT,
            caption TEXT,
            objects TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_user(username, password):
    conn = sqlite3.connect("app.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()


def get_user(username):
    conn = sqlite3.connect("app.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()
    return user


def save_result(username, image_name, caption, objects):
    conn = sqlite3.connect("app.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO results (username, image_name, caption, objects) VALUES (?, ?, ?, ?)",
        (username, image_name, caption, objects)
    )
    conn.commit()
    conn.close()


def get_user_results(username):
    conn = sqlite3.connect("app.db")
    c = conn.cursor()
    c.execute("SELECT image_name, caption, objects FROM results WHERE username=?", (username,))
    results = c.fetchall()
    conn.close()
    return results
