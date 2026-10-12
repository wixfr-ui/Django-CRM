import mysql.connector 

dataBase = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    passwd = ''
)

#cursor object 

cursorObject = dataBase.cursor()

#create db
cursorObject.execute ("CREATE DATABASE elderco")

print("All done!")
