#Implements all interceptor methods
from interceptorPattern.interceptor import *
from flask import render_template
class ConcreteInterceptor(Interceptor):
    def creditCardValidation(self,cardNumber):
        #Some processing to be done
        return render_template('success.html')