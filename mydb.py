import mysql.connector


dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
)


# prepare a cursor Object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE django")

print("All Done!")
