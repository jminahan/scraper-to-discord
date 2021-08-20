import abc
from src.Models.BSM.article import Article
from src.Interfaces.scaperconfig_interface import ScraperConfig

class DatabaseInterface(abc.ABC):
    def __init__(self):
        """
        Purpose: This class is used to define what functionality this program
            will need from a database in order to work...

        Example: SimpleFile, MongoDb
        """
        pass

    @abc.abstractclassmethod
    def getLastArticle(self, scraperConfig : ScraperConfig) -> Article:
        """
            Purpose : Get the Last Article associated with the ScraperConfig. This will most often be used
                if the program needs to check whether the most recent article is a new article or not
        """
        pass

    @abc.abstractclassmethod
    def putArticle(self, scraperConfig: ScraperConfig, article : Article):
        """
            Purpose : Update the database to the most recent article associated with the scraperconfig.
        """
        pass