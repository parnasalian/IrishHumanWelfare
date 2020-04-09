from donations import cash_donations
from flask import Flask

app = Flask(__name__)

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
            if request.method == "POST":
                movieName = request.args.get('movie_name')
                theaterLocation = request.args.get('theaterLocation')
                isGiftVoucher = request.args.get('giftVoucher')
                print("Is gift voucher?",isGiftVoucher)
                logger = logging.getLogger(__name__)   #instance of logger
                logger.info('Login page accessed')
            return render_template("login.html", movieName = movieName,isGiftVoucher = isGiftVoucher,theaterLocation = theaterLocation)

class Register:


if __name__ == "main":
    app.secret_key = os.urandom(24)
    app.run(debug=True,host='127.0.0.1', port=5000, threaded=True)