#Triggers concrete interceptors



def registerInterceptors():
    add interceptors to a lists or something
    return interceptorList

def removeInterceptors():
    remove interceptors

def dispatch(co): #Dispatches interceptor method when event occurs
    for interceptor in interceptorList:
        if event == interceptor:   #what should be compared for iteration
            ci = ConcreteInterceptor()
            ci.eventaction(co)