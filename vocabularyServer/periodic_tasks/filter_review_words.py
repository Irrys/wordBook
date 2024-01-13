
from config import WORDS_DOCUMENT, REVIEW_WORDS_DOCUMENT
from constants import REVIEW_INTERVALS
from clients.mongo_client import get_client
import re
import datetime


async def filter_review_words():
    # clear old review words
    pattern = re.compile(r".*?", re.IGNORECASE)
    client = get_client(REVIEW_WORDS_DOCUMENT)
    await client.delete_many(_filter={"name": pattern})

    client = get_client(WORDS_DOCUMENT)
    words = await client.find_all()
    review_words = []
    now = datetime.datetime.now()
    for word in words:
        if now >= word["review_time"] + \
                datetime.timedelta(REVIEW_INTERVALS.get(word["level"], REVIEW_INTERVALS["default"])):
            review_words.append(word)

    if review_words:
        client = get_client(REVIEW_WORDS_DOCUMENT)
        res = await client.insert_many(review_words)
        return res
