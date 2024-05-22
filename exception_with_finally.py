import sqlite3

conn = None

try:
    conn = sqlite3.connect('/foo/bar/badger.db')
except sqlite3.OperationalError as err:
    print(err)
    exit()
else:
    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute("insert ... into badgers")
    except sqlite3.DatabaseError as err:
        conn.rollback()
    else:
        conn.commit()
    finally:
        if cursor is not None:
            cursor.close()

finally:
    if conn is not None:
        conn.close()