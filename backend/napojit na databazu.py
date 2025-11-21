import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",     
    database="prototyp"
)

cursor = connection.cursor()
cursor.execute("SELECT message FROM test LIMIT 1")

row = cursor.fetchone()
print("Z databázy:", row[0])

cursor.close()
connection.close()
