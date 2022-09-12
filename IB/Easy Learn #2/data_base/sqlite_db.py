import sqlite3
# from create_bot import dp, bot

def sql_read_tesing():

    base = sqlite3.connect('easy_learn.db')
    cur = base.cursor()

    data = cur.execute('SELECT * FROM testing').fetchall()
    return data
