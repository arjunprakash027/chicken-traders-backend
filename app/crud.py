from db import get_db

def insert_value(itemname, date, weight, transtype, remark):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO data VALUES (?, ?, ?, ?, ?)", (itemname, date, weight, transtype, remark))
    conn.commit()

def update_value(itemname, date, weight, transtype, remark):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE data SET weight = ?, transtype = ?, remark = ?,date=? WHERE itemname = ?", (weight, transtype, remark, date, itemname))
    conn.commit()

def delete_value(itemname):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM data WHERE itemname = ?", (itemname,))
    conn.commit()

def get_all_values():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM data")
    rows = cursor.fetchall()
    return rows

def get_value(itemname):
    conn = get_db()
    cursor = conn.execute("SELECT * FROM data WHERE itemname = ?", (itemname,))
    rows = cursor.fetchall()
    return rows

