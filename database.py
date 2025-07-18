import  sqlite3


conn = sqlite3.connect("users.db")
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    Id INT PRIMARY KEY,
    name VARCHAR (50),
    balance INT,
    winstreak INT
    )
''')
conn.commit()

def add_user(user_id, name, balance, winstreak):
    cursor.execute ('''
        INSERT INTO users (id, name, age, like_bots)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET
            name = excluded.name,
            balance = excluded.balance,
            winstreak = excluded.winstreak
       ''',  (user_id, name, balance, winstreak))
    conn.commit()

def select_balance(user_id):
    a = cursor.execute('''
    SELECT balance FROM users
    where Id = ?
    ''',(user_id,))
    return a.fetchall()

def popoln(user_id, money):
    a = cursor.execute('''
    UPDATE users
    SET balance = balance + ?
    WHERE Id = ?
    ''',(user_id,money))
    conn.commit()
