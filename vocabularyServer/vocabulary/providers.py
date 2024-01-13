
from clients.mongo_client import get_client
from tools import format_response
from webcrawler import crawler
import config


class Vocabulary:

    @staticmethod
    @format_response
    async def search_word(word: str):
        # 1. try to find the word in mongoDB
        # import pdb; pdb.set_trace()
        mongo_client = get_client(config.WORDS_DOCUMENT)
        _filter = {"name": word}
        word_info = await mongo_client.find_one(_filter)
        if word_info:
            return word_info

        # 2. search the word on online dictionary
        word_info = crawler.crawl(word)

        # 3. store definitions of the word into mongoDB
        await mongo_client.insert_one(word_info)
        return word_info

    @staticmethod
    @format_response
    async def list_words():
        mongo_client = get_client(config.WORDS_DOCUMENT)
        words = await mongo_client.find_all()
        return words

    @staticmethod
    @format_response
    async def list_review_words():
        mongo_client = get_client(config.REVIEW_WORDS_DOCUMENT)
        words = await mongo_client.find_all()
        return words

    @staticmethod
    @format_response
    async def update_word(word, word_update):
        mongo_client = get_client(config.WORDS_DOCUMENT)
        _filter = {"name": word}
        update = {"$set": word_update.to_dict()}
        res = await mongo_client.update_one(_filter, update)
        return res


