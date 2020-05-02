#!/usr/bin/env python
from dao.dao import *
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
    def __init__(self):
        self.testList = []
    def process(self,message):
        self.testList.append(message.loc)

class getCategory(Filter):
    def process(self,message):
        location = getLocation()
        location.testList.append(message.category)
        

class getMode(Filter):

    def process(self,message):
        location = getLocation()
        location.testList.append(message.mode)
        print("Finalllll",list3)
        db = DataBase()
        db.leftoverDetailsToDb(list3)
        pass
