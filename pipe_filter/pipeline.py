#!/usr/bin/env python

class Pipeline(object):
    def __init__(self):
        self.filters = []
        pass

    def connect(self, filter):
        self.filters.append(filter)
        return self

    def execute(self, message):
        for filter in self.filters:
            filter.process(message)