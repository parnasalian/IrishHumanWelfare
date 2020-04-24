#Triggers concrete interceptors

class Dispatcher():
    def __init__(self):
        self.interceptorList = []
    
    def registerInterceptors(self,interceptor):
        self.interceptorList.append(interceptor)
        print(self.interceptorList)


    def dispatch(self,cardNumber): #Dispatches interceptor method when event occurs
        for interceptor in self.interceptorList:
            print("Dispatch")
            return interceptor.creditCardValidation(cardNumber)