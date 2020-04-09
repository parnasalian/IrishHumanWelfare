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
        username_form  = request.form['username']
        password_form  = request.form['password'] 
        cur.execute("SELECT COUNT(1) FROM user_info WHERE vist_name = %s;", [username_form]) # CHECKS IF USERNAME EXSIST
        if cur.fetchone()[0]:
            cur.execute("SELECT user_password FROM user_info WHERE username = %s;", [username_form]) # FETCH THE HASHED PASSWORD
            for row in cur.fetchall():
                if password_form  == row[0]:
                    session['user'] = username_form
                    print("PASSWORD is correct...")
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
    @app.route("/register")
    def register():
        return render_template("register.html")


    @app.route("/processRegistration",methods = ['POST','GET'])
    def processRegistration():
        if g.user:
            global dbconn
            if request.method == "POST":
                print("Enter!!")
                custName = request.form['Username']
                print(custName)
                custEmail = request.form['Email']
                custPassword = request.form['Password']
                custAddress = request.form['Address']
                custPhoneNumber = request.form['PhoneNumber']
            cur=dbcon.cursor()
            query = "INSERT INTO user_info(username,email,phone,user_password,address) VALUES(%s,%s,%s,%s,%s)"
            args = (custName, custEmail,  custPhoneNumber, custPassword, custAddress)
            cur.execute(query,args)
            dbcon.commit()
            print("Row inserted...")
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))

class HomePage:
    @app.route("/index", methods = ['POST','GET'])
    def indexPage():
        return render_template("index.html")



if __name__ == "main":
    app.secret_key = os.urandom(24)
    app.run(debug=True,host='127.0.0.1', port=5000, threaded=True)