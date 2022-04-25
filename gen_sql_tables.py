import mysql.connector

def generate_table():
    #establishing the connection
    conn = mysql.connector.connect(
    user='root', password='ubercharge1', host='localhost', database='dice_game'
    )

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Dropping EMPLOYEE table if already exists.
    cursor.execute("DROP TABLE IF EXISTS DICE_RESULTS")

    #Creating table as per requirement
    sql ='''create table DICE_RESULTS
(
	TRIALS int auto_increment,
	USER_DICE int not null,
	AI_DICE int not null,
	constraint DICE_RESULTS_pk
		primary key (TRIALS)
);
    )'''
    try:
        cursor.execute(sql)

    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
        
    print("Total number of rows in table: ", cursor.rowcount)
    #Closing the connection
    conn.close()