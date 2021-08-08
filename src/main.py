from impl.pineandroses_scraper import PineAndRosesScraper

##Configs
from impl.pineandroses_config import PineAndRosesConfig


def initializeConfigs():
    configs = {
        "pr" : PineAndRosesConfig("PineAndRosesScraper", "https://pineandroses.org")
    }
    return configs



def main():
    configs = initializeConfigs()

    scraper = PineAndRosesScraper(configs["pr"])
    print(scraper.scrape())


main()
