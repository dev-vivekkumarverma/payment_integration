import sqlite3

def get_db_connection(dbPath:str)->sqlite3.Connection:
    """accepts the sqlite database path and returns the database connection"""
    conn = sqlite3.connect(dbPath)
    conn.row_factory = sqlite3.Row
    return conn



def init_db(dbPath:str)->bool:
    """accepts the sqlite database path and returns True if database initiated successfully or False otherwise"""
    conn=None
    try:
        conn = get_db_connection(dbPath)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS payments (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id TEXT,
                            amount REAL,
                            currency TEXT,
                            status TEXT,
                            razorpay_payment_id TEXT,
                            created_at TEXT
                        )''')
        conn.commit()
        return True
    except Exception as e:
        print(f"Error::{str(e)}")
        return False
    finally:
        if conn:
            conn.close()