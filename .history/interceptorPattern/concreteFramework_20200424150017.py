#integrate dispatcher that allows applications to intercept events
#interceptor has methods that is invoked by this class via dispatcher when the event occurs
from interceptorPattern.contextObject import *
from interceptorPattern.dispatcher import Dispatcher
class ConcreteFramework():
    def processtransaction(self,cardNumber):
        co = ContextObject(cardNumber)

    def notifyDispatcher(self):
        co = ContextObject()
        dispatcher = Dispatcher()
        return dispatcher.dispatch(co)