import asyncio
import motor.motor_asyncio
from config import WORDS_DOCUMENT, REVIEW_WORDS_DOCUMENT
from constants import REVIEW_INTERVALS
from clients.mongo_client import get_client
import datetime
from pydantic import Field
import re

async def example():

    # Insert a document
    # result = await collection.insert_one({'key': 'value'})
    # print(result.__dir__())
    # print('Inserted document with id %s' % result.inserted_id)

    # Query for a document
    # document = await collection.find_one({'name': 'hello'})
    client = get_client(WORDS_DOCUMENT)
    # words = await client.find_all()
    # review_words = []
    # now = datetime.datetime.now()
    # # import pdb
    # # pdb.set_trace()
    # for word in words:
    #     if now >= word["review_time"] + datetime.timedelta(REVIEW_INTERVALS[word["level"]]):
    #         review_words.append(word)
    #
    #
    client = get_client(REVIEW_WORDS_DOCUMENT)
    pattern = re.compile(r".*?", re.IGNORECASE)
    res = await client.delete_many(_filter={"name": pattern})
    print(res)
    # res = await client.insert_many(review_words)
    # print(res)
    # time = document["review_time"]
    # print(time, type(time))
    # cursor = collection.find()
    # result = []
    # async for document in cursor:
    #     result.append(document)
    # result = await cursor.to_list(length=10)
    # print(result)

# Run the event loop
# loop = asyncio.get_event_loop()
# loop.run_until_complete(example())

from periodic_tasks import Task

task = Task()
task.start()
