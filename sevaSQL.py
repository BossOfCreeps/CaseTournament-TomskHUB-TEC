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
        '''print("seva")
    
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
        records=select_sql()
        cursor.execute("INSERT INTO `maintable` VALUES (" + str(records[len(records)-1][0] + 1) + ", " + data + ");")
        connection.commit()
        connection.close()
        cursor.close()
        return "insert_into_sql"
    except Error as e:
        return "Error reading data from MySQL table"+str(e)

def delete_sql(name):
    try:
        connection = mysql.connector.connect(host='34.90.47.156', database='testdb', user='seva', password='rachis')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM maintable WHERE name = '"+name+"';")
        connection.commit()
        connection.close()
        cursor.close()
        return "delete_sql"
    except Error as e:
        return "Error reading data from MySQL table"+str(e)

def delete_all_sql():
    try:
        connection = mysql.connector.connect(host='34.90.47.156', database='testdb', user='seva', password='rachis')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM maintable")
        connection.commit()
        connection.close()
        cursor.close()
        return "delete_all_sql"
    except Error as e:
        return "Error reading data from MySQL table"+str(e)

def find_sql(name):
    try:
        connection = mysql.connector.connect(host='34.90.47.156', database='testdb', user='seva', password='rachis')
        sql_select_Query = "select * from maintable where name='"+name+"';"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        connection.close()
        cursor.close()
        '''print("seva")

        for row in records:
            for col in row:
                print(col)
        '''
        return records
    except Error as e:
        return "Error reading data from MySQL table" + str(e)

def update_sql(name, date, weight, dimensions_x, dimensions_y, dimensions_z, composition, qual_control):
    try:
        connection = mysql.connector.connect(host='34.90.47.156', database='testdb', user='seva', password='rachis')
        cursor = connection.cursor()
        cursor.execute("UPDATE maintable "
                       "SET name='"+name+"', date='"+date+"', weight="+weight+", dimensions_x="+dimensions_x+", "
                        "dimensions_y="+dimensions_y+", dimensions_z="+dimensions_z+", composition='"+composition+"', qual_control="+qual_control+" WHERE name = '"+name+"';")
        connection.commit()
        connection.close()
        cursor.close()
        return "delete_sql"
    except Error as e:
        return "Error reading data from MySQL table"+str(e)


data = "'pasha', '1997-10-04', 3.14, 0.1, 0.2, 0.4, 'oxygen2', 1"
#print(delete_sql("polya_name"))
#print(select_sql())
#print(insert_into_sql(data))
#print(delete_all_sql())


