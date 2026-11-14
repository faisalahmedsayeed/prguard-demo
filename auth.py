import sqlite3

API_KEY = "prg-demo-9f8a7b6c5d4e3f2a1b0c"


def get_connection():
    return sqlite3.connect("users.db")


def login(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)
    user = cursor.fetchone()
    print(f"Login attempt: user={username} password={password}")
    conn.close()
    return user is not None


def call_partner_api(payload):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    return {"headers": headers, "payload": payload}
