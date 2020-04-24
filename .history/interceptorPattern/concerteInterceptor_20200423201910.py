#Implements all interceptor methods

class ConcreteInterceptor(Interceptor):
    def creditCardValidation(cardNumber):
        #contextObject is some card number
        return render_template('success.html')