import mysql.connector

def gen_round_tb():
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
    cursor.execute('DROP TABLE IF EXISTS ROUND_INFO')

    #Creating table
    sql = '''create table ROUND_INFO(
                NUM int auto_increment,
                TURN int not null,
                MOVE varchar(200) not null,
                OPPO_OPEN int not null,
                constraint DICE_RESULTS_pk
                    primary key (NUM));'''
    try:
        cursor.execute(sql)
        ''' print('table created') '''
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
    
    #Show tables
    ''' cursor.execute("show tables")
    for tb in cursor:
        print(tb) '''

    #Closing the connection
    cursor.close()
