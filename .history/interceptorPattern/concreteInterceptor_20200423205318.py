#Implements all interceptor methods
from interceptorPattern.interceptor import *
class ConcreteInterceptor(Interceptor):
    def creditCardValidation(cardNumber):
        #contextObject is some card number
        return render_template('success.html')