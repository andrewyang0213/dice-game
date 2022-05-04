import mysql.connector

def insTurn(turn):
    try:
        #establishing the connection
        conn = mysql.connector.connect(
            user='root', password='ubercharge1', host='localhost', database='dice_game'
            )
        cursor = conn.cursor()
        sql = '''insert into ROUND_INFO(TURN) values (%s)'''
        cursor.execute(sql, turn)
        conn.commit()
    finally:
    #Closing the connection
        if conn.is_connected():
            conn.close()
            ''' print("MySQL connection is closed") '''

def updateMove(move, num):
    try:
        #establishing the connection
        conn = mysql.connector.connect(
            user='root', password='ubercharge1', host='localhost', database='dice_game'
            )
        cursor = conn.cursor()
        sql = '''update ROUND_INFO set MOVE = (%s) where NUM = (%s)'''
        cursor.executemany(sql, [(move, num)])
        conn.commit()
    finally:
    #Closing the connection
        if conn.is_connected():
            conn.close()
            ''' print("MySQL connection is closed") '''

def insOpen(open):
    try:
        #establishing the connection
        conn = mysql.connector.connect(
            user='root', password='ubercharge1', host='localhost', database='dice_game'
            )
        cursor = conn.cursor()
        sql = '''insert into ROUND_INFO(OPPO_OPEN) values (%s)'''
        cursor.execute(sql, open)
        conn.commit()
    finally:
    #Closing the connection
        if conn.is_connected():
            conn.close()
            ''' print("MySQL connection is closed") '''
