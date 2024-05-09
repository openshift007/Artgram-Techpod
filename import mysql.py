import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
#----------------------------------------------
def DBConnection() :
    ##### Open the Word doc attached and do those things first.

    DbName = 'SP2024Python'
    try: 
       conn = mysql.connector.connect(user='root',
                                 password='Root1234!', 
                                 host='localhost',
                                 database=DbName)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
           print("Something wrong with username/password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
           print("Database does not exist")
        else:
           print(err)

    return conn
#-----------------------------------------------
def Create_Table_Empl(conn) :
  
    TABLES = {}
    TABLES['Employees_Guha'] = (
        "CREATE TABLE `Employee_Guha` ("
        "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
        "  `birth_date` date NOT NULL,"
        "  `first_name` varchar(14) NOT NULL,"
        "  `last_name` varchar(16) NOT NULL,"
        "  `gender` enum('M','F') NOT NULL,"
        "  `hire_date` date NOT NULL,"
        "  PRIMARY KEY (`emp_no`)"
        ")")

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            crsr = conn.cursor()
            crsr.execute(table_description)  
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
            print()
        else:
            print("OK")
#------------------------------------------




