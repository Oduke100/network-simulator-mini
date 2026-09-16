from database import get_conn


#switch functions
def s_all():
	conn=get_conn()
	cursor=conn.cursor()

	cursor.execute(
		"SELECT * FROM switch"
			)

	switch=cursor.fetchall()
	conn.commit()
	conn.close()

	return switch

def s_specific(name):
	conn=get_conn()
	cursor=conn.cursor()

	cursor.execute(
		"SELECT * FROM switch WHERE name = ?", (name, )
			)

	switch=cursor.fetchone()
	conn.commit()
	conn.close()


	return switch

def s_remove(name):
	conn=get_conn()
	cursor=conn.cursor()

	cursor.execute(
		"DELETE FROM switch WHERE name = ?", (name, )
			)

	conn.commit()
	conn.close()


#station routes
def t_all(name):
	conn=get_conn()
	cursor=conn.cursor()

	cursor.execute(
		"SELECT * FROM station"
			)

	stations=cursor.fetchall()
	conn.commit()
	conn.close()

	return stations

def t_specific(name):
	conn=get_conn()
	cursor=conn.cursor()

	cursor.execute(
		"SELECT * FROM station WHERE name = ?", (name, )
			)

	stations=cursor.fetchone()
	conn.commit()
	conn.close()

	return stations

def t_remove(name):
	conn=get_conn()
	curosr=conn.cursor()

	cursor.execute(
		"DELETE FROM station WHERE name = ?", (name, )
			)

	conn.commit()
	conn.close()

	return {"message": "deleted successfully"}
