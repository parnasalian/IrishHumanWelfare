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
        getLocation.testList = []
    def process(self,message):
        getLocation.testList.append(message.loc)
        print("in loc",getLocation.testList)
    
class getCategory(getLocation,Filter):
    def __init__(self):
        self.testList = getLocation.testList
    def process(self,message):
        # location = getLocation()
        self.testList.append(message.category)
        print("in cat",self.testList)
        

class getMode(getCategory,Filter):
    def __init__(self,class_b):
        self.testList = getCategory.testList
    def process(self,message):
        # location = getLocation()
        self.testList.append(message.mode)
        print("Finalllll",self.testList)
        db = DataBase()
        db.leftoverDetailsToDb(self.testList)
        pass
