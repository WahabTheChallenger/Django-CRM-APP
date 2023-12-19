import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'something88'
)


cursorobject = database.cursor()

cursorobject.execute('CREATE DATABASE crmapp')

print('All Done!')







# 12345678910