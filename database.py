import os
import json
import sqlite3

path=os.path.expanduser("~/sandbox/network-simulator-mini/nsm.db")

def get_conn():
	conn=sqlite3.connect(path)
	return conn

# multiple lines needs tripple quotes, DO NOT FORGET!!!!
def init_db():
	conn=get_conn()
	cursor=conn.cursor()
	cursor.execute(
		"""CREATE TABLE IF NOT EXISTS switch (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		latitude REAL NOT NULL,
		longitude REAL NOT NULL,
		altitude REAL NOT NULL,
		country TEXT NOT NULL,
		country_code TEXT NOT NULL,
		created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""
	)
	conn.commit()
	conn.close()
