from donations import cash_donations
from flask import Flask

app = Flask(__name__)
dbcon=dbManager.databaseConnection()

class Session:
    @app.before_request
    def before_request():
        g.user = None
        if 'user' in session:
            g.user = session['user']



class Login:
    @app.route("/login",methods = ['POST','GET'])
    def login():
        if g.user:
            username_form = session['user']
            return redirect(url_for('processLogin',username_form = username_form))
        else:
            return render_template("login.html", movieName = movieName,isGiftVoucher = isGiftVoucher,theaterLocation = theaterLocation)
    
    @app.route("/processLogin",methods = ['POST','GET'])
    def processLogin():
        cur=dbcon.cursor()
        theaterList = []
        showTime = [] 
        movieName = request.args.get('movieName')
        if g.user:
            movieName = request.args.get('movieName')
            username_form = request.args.get('username_form')
            theaterLocation = request.args.get('theaterLocation')
            query = "SELECT theater_name,theater_time from theater where theater_location = %s;"
            cur.execute(query,[theaterLocation])
            data = cur.fetchall()
            for row in data:
                if row[0] not in theaterList:
                    theaterList.append(row[0])
                if row[1] not in showTime:
                    showTime.append(row[1])
            return render_template("bookMovie.html", username_form = username_form, movieName = movieName,theaterList = theaterList,showTime = showTime)
   
        elif request.method == 'POST':
            session.pop('user',None)
            username_form  = request.form['username']
            isGiftVoucher = request.args.get('isGiftVoucher')
            theaterLocation = request.args.get('theaterLocation')
            query = "SELECT theater_name,theater_time from theater where theater_location = %s;"
            cur.execute(query,[theaterLocation])
            data = cur.fetchall()
            for row in data:
                if row[0] not in theaterList:
                    theaterList.append(row[0])
                if row[1] not in showTime:
                    showTime.append(row[1])
            print("Is gift voucher?",isGiftVoucher)
            print(username_form)
            password_form  = request.form['password'] 
            cur.execute("SELECT COUNT(1) FROM visitor_login WHERE vist_name = %s;", [username_form]) # CHECKS IF USERNAME EXSIST
            if cur.fetchone()[0]:
                cur.execute("SELECT vist_password FROM visitor_login WHERE vist_name = %s;", [username_form]) # FETCH THE HASHED PASSWORD
                for row in cur.fetchall():
                    if password_form  == row[0] and isGiftVoucher == "yes":
                        return render_template("sendGiftVoucher.html")
                    elif password_form  == row[0]:
                        session['user'] = username_form
                        print("PASSWORD is correct...")
                        logger = logging.getLogger(__name__)   #instance of logger
                        logger.info('Login page processed')
                        return render_template("bookMovie.html", username_form = username_form, movieName = movieName,theaterList = theaterList,showTime = showTime)     
                    else:
                      return render_template("login.html")  
            return render_template("login.html")

    @app.route('/logout', methods = ['POST','GET'])
    def logout():
        session.pop('user',None)
        logger = logging.getLogger(__name__)   #instance of logger
        logger.info('Logout processed')
        return redirect(url_for('viewMovie'))


class Register:


if __name__ == "main":
    app.secret_key = os.urandom(24)
    app.run(debug=True,host='127.0.0.1', port=5000, threaded=True)