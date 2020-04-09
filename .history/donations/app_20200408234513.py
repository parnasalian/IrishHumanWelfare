from donations import cash_donations
from flask import Flask

app = Flask(__name__)




if __name__ == "main":
    app.secret_key = os.urandom(24)
    app.run(debug=True,host='127.0.0.1', port=5000, threaded=True)