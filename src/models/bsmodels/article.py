import datetime

class Article():
    def __init__(self):
        self.datetime = None
        self.content = None
        self.headline = None

    def build(self, datetime : datetime, content : str, headline : str):
        pass

    def build(self, info : dict):
        pass