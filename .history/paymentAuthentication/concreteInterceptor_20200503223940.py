#Implements all interceptor methods
from paymentAuthentication.interceptor import *
from flask import render_template
class ConcreteInterceptor2(Interceptor2):
    def creditCardValidation(self,contextobject):
        #Some processing to be done
        pattern = '^[973][0-9]{15}|[973][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'
        result = re.match(pattern, contextobject.cardNumber)
        if result:
            return render_template('success.html')
        else:
            return render_template('creditCardPayment.html')