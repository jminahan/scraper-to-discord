from src.Implementations.pineandroses_scraper import PineAndRosesScraper

##Util Object
from src.Implementations.articleformfactory import ArticleFormFactory
from src.Implementations.simplefile_databaseimplementation import SimpleFileDatabase

##Configs
from src.Implementations.pineandroses_config import PineAndRosesConfig

def initializeConfigs():
    configs = {
        "pr" : PineAndRosesConfig("PineAndRosesScraper", "https://pineandroses.org")
    }
    return configs

def initializeArticalGenerator():
    art_generator = ArticleFormFactory()
    return art_generator

def initializeDatabase():
    database = SimpleFileDatabase("./test.json")
    return database


def main():
    configs = initializeConfigs()
    art_generator = initializeArticalGenerator()
    database = initializeDatabase()
    scraper = PineAndRosesScraper(configs["pr"])
    art = art_generator.textContentToArticle(scraper.scrape()[0])
    database.putArticle(configs["pr"], art)
    


main()