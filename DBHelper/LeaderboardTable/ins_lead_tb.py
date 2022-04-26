import mysql.connector

def ins_lead_tb(user):
    try:
    #establishing the connection
        conn = mysql.connector.connect(
        user='root', password='ubercharge1', host='localhost', database='dice_game'
        )

        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        #Creating table as per requirement
        sql = '''insert into LEADERBOARD(PLAYER) values (%s)'''
        cursor.execute(sql, user)
        
        conn.commit()

    finally:
    #Closing the connection
        if conn.is_connected():
            conn.close()
            print("MySQL connection is closed")

