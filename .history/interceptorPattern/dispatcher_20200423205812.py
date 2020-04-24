#Triggers concrete interceptors

class Dispatcher():
    def __init__(self):
        self.interceptorList = []
    
    def registerInterceptors(object):
        interceptorList.append(object)

    def dispatch(cardNumber): #Dispatches interceptor method when event occurs
        for interceptor in interceptorList:
            interceptor.creditCardValidation(cardNumber)