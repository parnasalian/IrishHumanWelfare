#Triggers concrete interceptors

class Dispatcher():
    def __init__(self):
        self.interceptorList = []
    
    def registerInterceptors(self,interceptor):
        self.interceptorList.append(interceptor)

    def dispatch(cardNumber): #Dispatches interceptor method when event occurs
        for interceptor in self.interceptorList:
            interceptor.creditCardValidation(cardNumber)