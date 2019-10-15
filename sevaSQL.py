import mysql.connector
from mysql.connector import Error

def select_sql():
    try:
        connection = mysql.connector.connect(host='34.90.47.156', database='testdb', user='seva', password='rachis')
        sql_select_Query = "select * from maintable"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        connection.close()
        cursor.close()
        '''print(len(records))
        print("seva")
    
        for row in records:
            for col in row:
                print(col)
        '''
        return records
    except Error as e:
        return "Error reading data from MySQL table"+str(e)

def insert_into_sql(data):
    try:
        connection = mysql.connector.connect(host='34.90.47.156', database='testdb', user='seva', password='rachis')
        cursor = connection.cursor()
        # data = (len(select_sql()) + 1,) + data
        #print("INSERT INTO `maintable` VALUES (" + str(len(select_sql()) + 1) + ", " + data + ");")
        cursor.execute("INSERT INTO `maintable` VALUES (" + str(len(select_sql()) + 1) + ", " + data + ");")
        connection.commit()
        connection.close()
        cursor.close()
        return "insert_into_sql"
    except Error as e:
        return "Error reading data from MySQL table"+str(e)

def delete_sql():
    try:
        connection = mysql.connector.connect(host='34.90.47.156', database='testdb', user='seva', password='rachis')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM maintable")
        connection.commit()
        connection.close()
        cursor.close()
        return "delete_sql"
    except Error as e:
        return "Error reading data from MySQL table"+str(e)

#data = "'polya_name', '1997-10-04', 3.14, 0.1, 0.2, 0.4, 'oxygen2', 1"
print(select_sql())
#print(insert_into_sql(data))
#print(delete_sql())


