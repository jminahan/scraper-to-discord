from src.Models.BSM.article import Article
from datetime import datetime

class ArticleFormFactory():
    def __init__(self):
        pass
        
    def textContentToArticle(self, content : {}):
        """
        This function will take in content in the form of:

            {href, text} -> content

        and return an article object
        """
        art_obj = Article()
        art_obj.build(datetime.now(), "", content["text"])
        return art_obj

    def articleToMessageContent(self, article: Article):
        pass
