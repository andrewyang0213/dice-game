import mysql.connector

def ins_res_tb(id, user, ai, winner):
    try:
    #establishing the connection
        conn = mysql.connector.connect(
        user='root', password='ubercharge1', host='localhost', database='dice_game'
        )

        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        #Creating table as per requirement
        sql = '''insert into DICE_RESULTS(PLAYER_ID, PLAYER_DICE, AI_DICE, WINNER) values (%s, %s, %s, %s)'''
        cursor.executemany(sql, [(id, user, ai, winner)])
        
        conn.commit()

    finally:
    #Closing the connection
        if conn.is_connected():
            conn.close()
            print("MySQL connection is closed")

