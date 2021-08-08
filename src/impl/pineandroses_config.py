from custInterfaces.scaperconfig_interface import ScraperConfig

class PineAndRosesConfig(ScraperConfig):
    def __init__(self,
                scraper_name,
                scraper_title):
        super().__init__(scraper_name,scraper_title)