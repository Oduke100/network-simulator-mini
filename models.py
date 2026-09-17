from database import get_conn

# multiple lines needs tripple quotes, DO NOT FORGET!!!!
create_switch="""CREATE TABLE IF NOT EXISTS switch (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		latitude REAL NOT NULL,
		longitude REAL NOT NULL,
		altitude REAL NOT NULL,
		country TEXT NOT NULL,
		country_code TEXT NOT NULL,
		created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""

create_station="""CREATE TABLE IF NOT EXISTS station (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		switch_id INTEGER,
		name TEXT NOT NULL,
		latitude REAL NOT NULL,
		longitude REAL NOT NULL,
		altitude REAL NOT NULL,
		created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
		FOREIGN KEY (switch_id) REFERENCES switch(id))"""

def init_db():
	conn=get_conn()
	cursor=conn.cursor()
	cursor.execute(create_switch)
	cursor.execute(create_station)
	conn.commit()
	conn.close()
