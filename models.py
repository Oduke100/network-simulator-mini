from database import get_conn

# multiple lines needs tripple quotes, DO NOT FORGET!!!!
tables_execute="""CREATE TABLE IF NOT EXISTS switch (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		latitude REAL NOT NULL,
		longitude REAL NOT NULL,
		altitude REAL NOT NULL,
		country TEXT NOT NULL,
		country_code TEXT NOT NULL,
		created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""

def init_db():
	conn=get_conn()
	cursor=conn.cursor()
	cursor.execute(tables_execute)
	conn.commit()
	conn.close()
