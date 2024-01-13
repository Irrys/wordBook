from clients.Notion_client import Block, NotionClient
from constants import BlockType, Color
from config import REVIEW_WORDS_DOCUMENT
from clients.mongo_client import get_client
import asyncio


async def create_word_infos_block(parent_id, word_infos):
    infos_item = []
    for info in word_infos:
        definition = info["definition"]
        translation = info["translation"]

        # create a definition toggle block object.
        def_block = Block(BlockType.toggle)
        def_block.create_text(definition + "\n" + translation)
        def_block.B()

        # create an examples toggle block object.
        examples_block = Block(block_type=BlockType.toggle)
        examples_block.create_text("examples")

        examples = info["examples"]
        for example in examples:

            en = example[0]
            zh = example[1]
            en_block = Block(BlockType.bulleted_list_item)
            en_block.I()
            en_item = en_block.create_block(en + "\n" + zh, color=Color.red)

            examples_block.add_child(en_item)

        example_item = examples_block.create()
        def_block.add_child(example_item)
        def_item = def_block.create()
        infos_item.append(def_item)

    n_client = NotionClient()
    await n_client.creat_blocks(parent_id, infos_item)


async def create_words_toggle_block():

    # 1. get review words
    client = get_client(REVIEW_WORDS_DOCUMENT)
    words = await client.find_all()

    words_item = []
    ids = []
    create_words_coro = []

    n_client = NotionClient()

    # create words toggle block
    for word in words:
        word_block = Block(BlockType.toggle)
        word_block.B()
        word_item = word_block.create_block(word["name"])
        words_item.append(word_item)
    response = await n_client.creat_blocks("f09e34a80d8649f88cf3b5180ca1a77c", words_item)

    results = response["results"]
    for result in results:
        ids.append(result["id"])

    # add create word infos coro to coro list
    i = 0
    for word in words:
        coro = create_word_infos_block(ids[i], word["definitions"])
        create_words_coro.append(coro)
        i += 1

    # gather coro list to run it asynchronously in parallel
    await asyncio.gather(*create_words_coro)

