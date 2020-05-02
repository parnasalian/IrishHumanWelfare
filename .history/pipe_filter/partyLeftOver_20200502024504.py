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
        pipe.connect(getCategory())
        pipe.execute(retrieveFrequency(category))

    def mode(self,mode):
        pipe=Pipeline()
        pipe.connect(getMode())
        pipe.execute(retrieveMode(mode))
