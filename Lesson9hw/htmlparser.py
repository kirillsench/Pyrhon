import requests as r
from bs4 import BeautifulSoup as bs
from logger import Logger

class HtmlParser:
    def __init__(self, url: str):
        self.Url: str = url
        self.Result: dict = dict()
        self.logger = Logger()

    def NbuParse(self, tag: str, attribute: str):
        try:
            response = r.get(self.Url)
            markup = response.content
            htmlDoc = bs(markup, features="html.parser")
            tags = htmlDoc.find_all(tag, attrs={'class' : attribute})
            counter = 0
            for tag in tags:
                strValue = tag.text.strip().replace(',', '.')
                self.Result[counter] = float(strValue)
                counter += 1
        except Exception as e:
            self.logger.log_error('Error occurred while parsing HTML content: {}'.format(e))
            raise