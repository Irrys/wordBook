from webcrawler.settings import (
    USERAGENT,
    CAMBRIDGE_URLBASE,
    CAMBRIDGE_LABEL_CLASS,
)
from webcrawler.request import Crawler
from webcrawler.HTML_parser import CambridgeDicParser
from bs4 import BeautifulSoup
from datetime import datetime


def crawl(word: str):
    word_info = {}
    crawler = Crawler(
        url_base=CAMBRIDGE_URLBASE,
        user_agent=USERAGENT
    )
    parser = CambridgeDicParser(BeautifulSoup, CAMBRIDGE_LABEL_CLASS)
    content = crawler.request(word)
    parser.parse(content)
    word_info.update({"definitions": parser.definitions_info})
    word_info.update({"name": word})
    word_info.update({"level": 1})
    date = datetime.now()
    word_info.update({"review_time": date})
    return word_info

