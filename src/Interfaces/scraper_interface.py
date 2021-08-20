import abc
from src.Models.BSM.article import Article
from src.Utils.requestwrapper import RequestWrapper


class ScraperInterface(abc.ABC):
    def __init__(self, config):
        """
            Purpose: ScraperInterface defines what implementations will need to scrape a news source.
                For example, the front page of bloomberg looks different than the front page of nyt
        """
        self.config = config
        self.requestwrapper = RequestWrapper()

    @abc.abstractclassmethod
    def scrape(self) -> str:
        """
        """
        pass

    @abc.abstractclassmethod
    def getMostRecent(self):
        """
        """
        pass

    @abc.abstractclassmethod
    def getNewArticles(self, listOfArticles : [Article]):
        """
        """
        pass