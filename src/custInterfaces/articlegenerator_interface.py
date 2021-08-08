import abc
from models.bsmodels.article import Article

def ArticleGenerator(abc.ABC):
    def __init__(self):
        pass

    def textContentToArticle(self, content : str) -> Article:
        pass
