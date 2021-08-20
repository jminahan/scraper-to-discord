import datetime
import json
from src.Utils.jsondateencoder import DateTimeEncoder

class Article():
    def __init__(self):
        """
        """
        self.datetime = None
        self.content = None
        self.headline = None

    def build(self, datetime : datetime, content : str, headline : str):
        """
        """
        self.datetime = datetime
        self.content = content
        self.headline = headline

    def toJson(self) -> str:
        """
        """
        return json.dumps(self.__dict__, cls=DateTimeEncoder)

    def fromJson(self, input : str):
        """
        """
        pass

    def __str__(self):
        return json.dumps(self.__dict__, cls=DateTimeEncoder)
