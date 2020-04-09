import mysql.connector
class Database_connection:
    def dbconn():
        mydb = mysql.connector.connect(
        user='bc5865edd7a83b',
        password='c1f43ffa',
        host='eu-cdbr-west-02.cleardb.net',
        port=3306,
        database='heroku_dffdac2c032f563')
