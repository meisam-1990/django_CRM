import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'
    )

# prepare a curser object
cursorObj = db.cursor()

cursorObj.execute("CREATE DATABASE elderco")

print("All Done!!")