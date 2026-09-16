import os
import json
import sqlite3

path=os.path.expanduser("~/sandbox/network-simulator-mini/nsm.db")

def get_conn():
	conn=sqlite3.connect(path)
	return conn
