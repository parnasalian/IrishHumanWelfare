#!/usr/bin/env python

class Filter(object):
    """
        Base filter class which can take a message and alter the message appropriately.
        You define what happens with the message.
    """

    def __init__(self):
        pass

    def process(self, message):
        pass

class getLocation(Filter):
    testList = []
    def process(self,message):
        global testList
        testList.append(message.loc)

class getCategory(Filter):
    def process(self,message):
        global testList
        testList.append(message.category)
        

class getMode(Filter):

    def process(self,message):
        global testList
        testList.append(message.mode)
