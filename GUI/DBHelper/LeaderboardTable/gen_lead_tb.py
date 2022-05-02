import mysql.connector


def gen_lead_tb():
    #establishing the connection
    conn = mysql.connector.connect(
    user='root', password='ubercharge1', host='localhost', database='dice_game'
    )

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    ''' cursor.execute("show databases")
    for db in cursor:
        print(db) '''

    #Creating table
    sql = '''create table if not exists LEADERBOARD(
                        RANKING int not null, 
                        PLAYER varchar(200), 
                        WINS int not null, 
                        WIN_PERCENT int not null,
                        TOTAL_GAMES int)
            '''
    try:
        cursor.execute(sql)
        print('table created')
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
    
    #Show tables
    cursor.execute("show tables")
    for tb in cursor:
        print(tb)

    #Closing the connection
    cursor.close()