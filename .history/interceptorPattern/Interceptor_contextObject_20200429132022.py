from abc import ABCMeta, abstractstaticmethod
import sys
import logging
from contextlib import contextmanager ,ContextDecorator

class State(ContextDecorator):
    def __enter__(self):
        print('Logging started')
        return self

    def __exit__(self, *exc):
        print('Logging finished')
        return False 

class ContextObject():
    def __init__(self, user=" "): 
         self._user = user 
      
    # getter method 
    def get_value(self): 
        return self._user 
      
    # setter method 
    def set_value(self, username): 
        self._user = username

class IInterceptor(metaclass=ABCMeta):
    @abstractstaticmethod
    def log():
        pass
        #Donation Interface

class ConcreteInterceptor(IInterceptor):
    @State()
    def log(self,obj):
        # create logger

        logger = logging.getLogger(__name__)   #instance of logger
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

        logger.info('User has logged'+obj)


class Dispatcher:
    def __init__(self):
        self.inter=[]
        return self.inter

    def register(self,interceptor):
        self.inter.append(interceptor)


    def remove(self,interceptor):
        self.inter.remove(interceptor)

    def dispatch(self,obj):
        for i in self.inter:
            i.log(obj)

class ConcreteFramework():
    def event(self,user):
        ContextObject.set_value(self,user)
        obj=ContextObject.get_value(self) 
        Dispatcher.dispatch(self,obj)
