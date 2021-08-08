import abc
from models.bsmodels.article import Article
from utils.requestwrapper import RequestWrapper


class ScraperInterface(abc.ABC):
    def __init__(self, config):
        self.config = config
        self.requestwrapper = RequestWrapper()

    @abc.abstractclassmethod
    def scrape(self) -> str:
        """
        Hello World
        """
        pass

    @abc.abstractclassmethod
    def getMostRecent(self):
        pass

    @abc.abstractclassmethod
    def getNewArticles(self, listOfArticles : [Article]):
        pass