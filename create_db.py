import sqlite3
''' Convention : Names of tables will be plurals'''
def create_db():
    con = sqlite3.connect(database=r'bms.db') # connection
    cur = con.cursor() # cursor put in place
    cur.execute('''CREATE TABLE IF NOT EXISTS stakeholders (
                eid INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name TEXT, 
                last_name TEXT, 
                contact_1 TEXT, 
                contact_2 TEXT, 
                company_title TEXT, 
                company_name TEXT, 
                balance_type TEXT, 
                balance_amount INTEGER, 
                stakeholder_type TEXT, 
                address TEXT, 
                email TEXT
                )''')
    con.commit()

    cur.execute('''CREATE TABLE IF NOT EXISTS products (
                eid INTEGER PRIMARY KEY AUTOINCREMENT, 
                code TEXT UNIQUE,
                name TEXT,
                description TEXT,
                stock_current INTEGER,
                stock_min INTEGER
                retail_price INTEGER,
                retail_unit TEXT,
                wholsale_price INTEGER,
                wholsale_unit TEXT,
                purchase_price INTEGER,
                purchase_unit TEXT
                )''')
    con.commit()

    cur.execute('''CREATE TABLE IF NOT EXISTS services (
                eid INTEGER PRIMARY KEY AUTOINCREMENT, 
                code TEXT UNIQUE, 
                name TEXT,
                description TEXT,
                retail_price INTEGER,
                retail_unit TEXT,
                expense_price INTEGER)''')
    con.commit()

    cur.execute('''CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                stakeholder_id INTEGER,
                transaction_date DATE,
                amount REAL,
                            
                FOREIGN KEY (stakeholder_id) REFERENCES stakeholders(stakeholder_id)
                )''')
    con.commit()


create_db()