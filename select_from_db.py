from mysql.connector import MySQLConnection, Error
from read_config import read_db_config

def query_name():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM tbl_birth WHERE MONTH(birth) = MONTH(CURDATE()) AND DAYOFMONTH(birth) = DAYOFMONTH(CURDATE()); ")
        birth_date = cursor.fetchall()

        #for row in birth_date:
            #print(row)
        return birth_date
        #while row is not None:
        #    print(row)
        #    row = cursor.fetchone()

            #row += 1
            #return row

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def query_random_congrats():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT text FROM congrats")
        random_congrats = cursor.fetchall()
        return random_congrats

    except Error as err:
        print(err)

def getAllPersons():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tbl_birth")
        birth_date = cursor.fetchall()

        return birth_date

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()



