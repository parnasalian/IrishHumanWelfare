#Triggers concrete interceptors

class Dispatcher():
    def registerInterceptors(interceptor):
        #add interceptors to a lists or something
        interceptorList = []
        interceptorList.append(interceptor)

    def removeInterceptors():
        #remove interceptors

    def dispatch(cardNumber): #Dispatches interceptor method when event occurs
        interceptorList = Dispatcher.registerInterceptors()
        for interceptor in interceptorList:
            interceptor.creditCardValidation(cardNumber)