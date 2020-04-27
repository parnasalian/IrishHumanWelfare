#integrate dispatcher that allows applications to intercept events
#interceptor has methods that is invoked by this class via dispatcher when the event occurs
from interceptorPattern.contextObject import *
from interceptorPattern.dispatcher import Dispatcher
class ConcreteFramework():
    co = ContextObject()
    def processtransaction(self,cardNumber):
        self.co = ContextObject(cardNumber)

    def notifyDispatcher(self):
        dispatcher = Dispatcher()
        return dispatcher.dispatch(self.co)