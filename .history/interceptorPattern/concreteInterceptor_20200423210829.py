#Implements all interceptor methods
from interceptorPattern.interceptor import *
from flask import render_template
class ConcreteInterceptor(Interceptor):
    def creditCardValidation(cardNumber):
        #contextObject is some card number
        print("The card number is........",cardNumber)
        return render_template('success.html')