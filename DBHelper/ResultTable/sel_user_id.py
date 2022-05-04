import mysql.connector

def selUserId(userName):
    try:
    #establishing the connection
        conn = mysql.connector.connect(
        user='root', password='ubercharge1', host='localhost', database='dice_game'
        )

        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        #Creating table as per requirement
        sql = '''SELECT PLAYER_ID FROM LEADERBOARD where PLAYER = (%s)'''
        cursor.execute(sql, userName)
        result = cursor.fetchall()
        for row in result:
            string = "".join(filter(str.isdigit, str(row)))
    finally:
    #Closing the connection
        if conn.is_connected():
            conn.close()
            ''' print("MySQL connection is closed") '''
    return(string)
