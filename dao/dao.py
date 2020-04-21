from database.dbconn import Database_connection

class DataBase:
    def retrieveDonations():
        dictionary = {}
        dbcon=Database_connection.dbconn()
        cur=dbcon.cursor()
        cur.execute("SELECT * FROM DonationType") # FETCH THE HASHED PASSWORD
        for row in cur.fetchall():
            donation_type = row[1]
            keyword = row[2]
            dictionary = {**dictionary,**{donation_type:keyword}}
        return dictionary