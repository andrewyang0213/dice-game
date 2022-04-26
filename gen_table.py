import mysql.connector

def generate_table():
    #establishing the connection
    conn = mysql.connector.connect(
    user='root', password='ubercharge1', host='localhost', database='dice_game'
    )

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    ''' cursor.execute("show databases")
    for db in cursor:
        print(db) '''

    #Dropping table if already exists.
    cursor.execute('DROP TABLE IF EXISTS DICE_RESULTS')

    #Creating table
    sql = '''create table DICE_RESULTS(TRIALS int auto_increment, USER_DICE varchar(200), AI_DICE varchar(200), MOVES varchar(200), END_MOVE varchar(200), WINNER varchar(200), constraint DICE_RESULTS_pk primary key (TRIALS))'''
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
