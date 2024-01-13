from motor import motor_asyncio
import config


class Client:

    def __init__(self, uri: str, database: str, document: str):
        self.client = motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self.client[database]
        self.collection = self.db[document]

    async def find_one(self, _filter=None, fields=None):
        result = await self.collection.find_one(_filter, fields)
        return result

    async def find_all(self, _fileter=None, fields=None):
        cursor = self.collection.find(_fileter, fields)
        result = []
        async for document in cursor:
            result.append(document)
        return result

    async def find_many(self, _filter=None, fields=None, offset: int = 0, partition: int = 10):
        cursor = self.collection.find(_filter, fields).skip(offset).limit(partition)
        result = await cursor.to_list(length=partition)
        return result

    async def insert_one(self, data):
        result = await self.collection.insert_one(data)
        return result

    async def insert_many(self, data_list):
        result = await self.collection.insert_many(data_list)
        return result

    async def update_one(self, _filter, update):
        result = await self.collection.update_one(_filter, update)
        return result.raw_result

    async def update_many(self):
        pass

    async def delete_many(self, _filter):
        result = await self.collection.delete_many(_filter)
        return result


client_pool = {}


def get_client(document):
    client = client_pool.get(document)
    if not client:
        client = Client(config.MONGO_URI, config.DATABASE, document)
        client_pool[document] = client
    return client

