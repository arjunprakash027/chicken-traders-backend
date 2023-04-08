import sqlite3
DATABASE_NAME = "data.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    tables = [
        """
        CREATE TABLE IF NOT EXISTS data(
            itemname TEXT NOT NULL,
            date TEXT NOT NULL,
            weight INTEGER NOT NULL,
            transtype TEXT CHECK (transtype IN ('purchase','sale')),
            remark TEXT CHECK (LENGTH(remark) <= 300)
        );
        """
    ]

    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)



if __name__ == "__main__":
    create_tables() 

    #print all the values
    conn = get_db()
    cursor = conn.execute("SELECT * FROM data")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
