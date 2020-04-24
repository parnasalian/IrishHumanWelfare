#Triggers concrete interceptors

class Dispatcher():
    def __init__(self):
        self.interceptorList = []
    
    def registerInterceptors(self,interceptor):
        interceptorList.append(interceptor)

    def dispatch(cardNumber): #Dispatches interceptor method when event occurs
        for interceptor in interceptorList:
            interceptor.creditCardValidation(cardNumber)