import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(host='34.90.47.156',
                                         database='testdb',
                                         user='seva',
                                         password='rachis')
    sql_select_Query = "select * from maintable"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in Laptop is: ", cursor.rowcount)

    print("\nPrinting each laptop record")
    for row in records:
        for col in row:
            print("Id = ", col)

except Error as e:
    print("Error reading data from MySQL table", e)

finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")