#Implements all interceptor methods
from paymentAuthentication.interceptor import *
from flask import render_template
import re
class ConcreteInterceptor2(Interceptor2):
    def creditCardValidation(self,contextobject):
        #Some processing to be done
        pattern = '^(?:4[0-9]{12}(?:[0-9]{3})?|[25][1-7][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$'
        print("In ciii",contextobject.cardNumber)
        result = re.match(pattern, contextobject.cardNumber)
        print(result)
        if result:
            return render_template('success.html')
        else:
            return render_template('creditCardPayment.html')