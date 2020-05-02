from pipe_filter.pipeline import *
from pipe_filter.filter import *
from pipe_filter.message import *

class Fooddonate:

    def location(self,location):
        pipe=Pipeline()
        pipe.connect(getLocation())
        pipe.execute(retrieveLocation(location))

    def category(self,category):
        pipe=Pipeline()
        loc = getLocation()
        pipe.connect(getCategory(loc))
        pipe.execute(retrieveFrequency(category))

    def mode(self,mode):
        cat = getCategory()
        pipe=Pipeline()
        pipe.connect(getMode(cat))
        pipe.execute(retrieveMode(mode))
