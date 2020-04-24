#Defines app services
#integrate dispatcher that allows applications to intercept events
# exposes events
# interceptor has methods that is invoked by this class via dispatcher when the event occurs








def somemethod(someevent):
    co = contextObject() #In this case the context object can contain information related to the event that triggered its creation.
    dispatcher = Dispatcher()

    dispatcher.dispatch(co)