#Triggers concrete interceptors

class Dispatcher:
    interceptorList = []
    def _init_(self):
        self.interceptorList = []
        return self.interceptorList
    
    def registerInterceptors(self,interceptor):
        self.interceptorList.append(interceptor)
        print("Interceptor List")
        print(self.interceptorList)


    def dispatch(self,cardNumber): #Dispatches interceptor method when event occurs
        print("Printing the list",self.interceptorList)
        for interceptor in self.interceptorList:
            print("Dispatch")
            return interceptor.creditCardValidation(cardNumber)