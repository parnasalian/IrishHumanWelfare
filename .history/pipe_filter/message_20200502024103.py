#!/usr/bin/env python

class Message(object):
    """
        Base type of a message sent through the pipeline.
        Define some attributes and methods to form your message.
        I suggest you don't alter this class. You're are free to do so, of course. It's your own decision.
        Though, I suggest you create your own message type and let it inherit from this class.
    """
    pass

class retrieveLocation(Message):
    def __init__(self,loc):
        self.loc=loc
        

class retrieveFrequency(Message):
    def __init__(self,category):
        self.category=category
        

class retrieveMode(Message):
    def __init__(self,mode):
        self.mode=mode
