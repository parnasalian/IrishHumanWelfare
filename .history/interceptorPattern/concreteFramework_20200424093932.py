#integrate dispatcher that allows applications to intercept events
# interceptor has methods that is invoked by this class via dispatcher when the event occurs

from interceptorPattern.dispatcher import Dispatcher
class ConcreteFramework():
    def notifyDispatcher(self,cardNumber):
        dispatcher = Dispatcher()
        print("Concrete Framework")
        return dispatcher.dispatch(cardNumber)