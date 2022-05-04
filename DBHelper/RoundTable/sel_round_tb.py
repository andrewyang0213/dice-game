import mysql.connector

def selRoundTurn():
    #establishing the connection
    conn = mysql.connector.connect(
        user='root', password='ubercharge1', host='localhost', database='dice_game'
        )
    cursor = conn.cursor()
    sql = '''SELECT TURN FROM ROUNDTABLE'''
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        string = "".join(filter(str.isdigit, str(row)))
    return(string)

def selUserMove():
    #establishing the connection
    conn = mysql.connector.connect(
        user='root', password='ubercharge1', host='localhost', database='dice_game'
        )
    cursor = conn.cursor()
    sql = '''SELECT USER_MOVE FROM ROUNDTABLE'''
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        string = "".join(filter(str.isdigit, str(row)))
    #Closing the connection
    if conn.is_connected():
        conn.close()
    ''' print("MySQL connection is closed") '''
    return(string)

def selOpen():
    #establishing the connection
    conn = mysql.connector.connect(
        user='root', password='ubercharge1', host='localhost', database='dice_game'
        )
    cursor = conn.cursor()
    sql = '''SELECT OPPO_OPEN FROM ROUNDTABLE'''
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        string = "".join(filter(str.isdigit, str(row)))
    #Closing the connection
    if conn.is_connected():
        conn.close()
    ''' print("MySQL connection is closed") '''
    return(string)

