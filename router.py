from database import get_conn

def all():

	conn=get_conn()
	cursor=conn.cursor()

	cursor.execute(
		"SELECT * FROM switch"
			)

	switch=cursor.fetchall()
	conn.commit()
	conn.close()

	return switch

def specific(name):

	conn=get_conn()
	cursor=conn.cursor()

	cursor.execute(
		"SELECT * FROM switch WHERE name = ?", (name, )
			)

	switch=cursor.fetchone()
	conn.commit()
	conn.close()


	return switch

def remove(name):

	conn=get_conn()
	cursor=conn.cursor()

	cursor.execute(
		"DELETE FROM switch WHERE name = ?", (name, )
			)

	#confirmation=f"{name} switch decomissioned successfully"
	conn.commit()
	conn.close()

	#return confirmation

