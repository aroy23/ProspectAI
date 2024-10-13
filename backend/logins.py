import sqlite3

def db_add(username:str, email:str, password: str):
    conn = sqlite3.connect('logins.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_data(
        username TEXT UNIQUE,
        email TEXT UNIQUE,
        password TEXT
    )
    ''')

    conn.commit()

    cursor.execute('''
    INSERT INTO user_data (username, email, password)
    VALUES (?, ?, ?)
    ''', (username, email, password))

    conn.commit()

    conn.close()

def db_login(username: str, password: str):
    conn = sqlite3.connect("logins.db")
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM user_data WHERE username = ? AND password = ?
    ''', (username, password))

    user = cursor.fetchone()

    conn.close()

    if user:
        return True
    else:
        return False
    
def db_remove(email:str):
    conn = sqlite3.connect('backend/logins.db')
    cursor = conn.cursor()

    cursor.execute('''DELETE FROM user_data where email = ?''', (email,))

    conn.commit()
    conn.close()