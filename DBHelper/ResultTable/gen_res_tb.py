import mysql.connector

def gen_res_tb():
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
    sql = '''create table DICE_RESULTS(
                TRIALS int auto_increment,
                PLAYER_ID int not null,
                PLAYER_DICE varchar(200) not null,
                AI_DICE varchar(200) not null,
                PLAYER_MOVE varchar(200) not null,
                AI_MOVE varchar(200) not null,
                WINNER varchar(200) not null,
                constraint DICE_RESULTS_pk
                    primary key (TRIALS),
                constraint DICE_RESULTS_LEADERBOARD_PLAYER_ID_fk
                    foreign key (PLAYER_ID) references LEADERBOARD (PLAYER_ID) 
                    on UPDATE CASCADE 
                    on DELETE CASCADE);'''
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
