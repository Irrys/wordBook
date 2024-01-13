from fastapi import APIRouter
from vocabulary.providers import Vocabulary
from vocabulary.models import WordUpdate

v_router = APIRouter()


@v_router.get("/vocabulary/words")
async def list_words():
    return await Vocabulary.list_words()


@v_router.get("/vocabulary/review-words")
async def list_review_words():
    return await Vocabulary.list_review_words()


@v_router.get("/vocabulary/{word}")
async def search_word(word: str):
    return await Vocabulary.search_word(word)


@v_router.put("/vocabulary/{word}")
async def update_word(word: str, word_update: WordUpdate):
    return await Vocabulary.update_word(word, word_update)
