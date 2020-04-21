from database.dbconn import Database_connection

class DataBase:
    dbcon=Database_connection.dbconn()
    cur=dbcon.cursor()
    def retrieveDonations():
        dictionary = {}
        cur.execute("SELECT * FROM DonationType") # FETCH THE HASHED PASSWORD
        for row in cur.fetchall():
            donation_type = row[1]
            keyword = row[2]
            dictionary = {**dictionary,**{donation_type:keyword}}
        return dictionary
    
    def getPasswordForLogin(username_form):
        cur.execute("SELECT COUNT(1) FROM user_info WHERE username = %s;", [username_form]) # CHECKS IF USERNAME EXSIST
        if cur.fetchone()[0]:
            cur.execute("SELECT user_password FROM user_info WHERE username = %s;", [username_form]) # FETCH THE HASHED PASSWORD
            for row in cur.fetchall():
                dbPassword = row[0]
        return dbPassword