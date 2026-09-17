from database import get_conn

"""
syntax shout:
    SELECT column1, column2 FROM table name
    SELECT column1, column2 FROM table name WHERE condition
    
"""

def switches():

    conn=get_conn()
    cursor=conn.cursor()

    cursor.execute(
        "SELECT name FROM switch"
    )

    data=cursor.fetchall()
    data = [row[0] for row in data] #this is data formatting for the switch.create() function

    conn.commit()
    conn.close()

    return data


# data=switches()
# print(data)