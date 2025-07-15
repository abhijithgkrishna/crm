import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="test1234",

)

cursorObject = database.cursor()
cursorObject.execute("CREATE DATABASE crm_db")

print("Database created successfully")