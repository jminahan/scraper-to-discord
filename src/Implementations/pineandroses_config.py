from src.Interfaces.scaperconfig_interface import ScraperConfig

class PineAndRosesConfig(ScraperConfig):
    def __init__(self,
    scraper_name,
    scraper_title):
        """
            The purpose of this class is to have a specific implementation of ScraperConfig for Pines and roses

            In the future, I may move the logic of scraper (aka, steps to parse, aka "look in h3 of name xyz for content") into here.
            in order to have a single Scraper class that just takes in that info per config
        """
        super().__init__(scraper_name,scraper_title)