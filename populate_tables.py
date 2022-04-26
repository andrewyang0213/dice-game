import mysql.connector

def populate():
    try:
    #establishing the connection
        conn = mysql.connector.connect(
        user='root', password='ubercharge1', host='localhost', database='dice_game'
        )

        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        #Dropping EMPLOYEE table if already exists.
        cursor.execute("DROP TABLE IF EXISTS DICE_RESULTS")

        #Creating table as per requirement
        sql = '''insert into DICE_RESULTS(USER_DICE, AI_DICE) values (1, 2)'''
        cursor.execute(sql)

    finally:
    #Closing the connection
        if conn.is_connected():
            conn.close()
            print("MySQL connection is closed")
