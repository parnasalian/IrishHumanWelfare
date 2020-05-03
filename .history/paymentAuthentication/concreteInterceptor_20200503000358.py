#Implements all interceptor methods
from paymentAuthentication.interceptor import *
from flask import render_template
class ConcreteInterceptor2(Interceptor2):
    def creditCardValidation(self,contextobject):
        #Some processing to be done
        cardNumber = contextobject.getCardNumber()
        print("Card Number :", cardNumber)
        return render_template('success.html')