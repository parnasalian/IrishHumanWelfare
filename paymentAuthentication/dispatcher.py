#Triggers concrete interceptors
class Dispatcher2:
    interceptorList = []
    def _init_(self):
        self.interceptorList = []
        return self.interceptorList
    
    def registerInterceptors(self,interceptor):
        self.interceptorList.append(interceptor)
        print(self.interceptorList)


    def dispatch(self,contextobject): #Dispatches interceptor method when event occurs
        for interceptor in self.interceptorList:
            return interceptor.creditCardValidation(contextobject)