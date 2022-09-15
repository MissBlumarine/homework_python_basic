import typing
import random
from pydantic import BaseModel
from pydantic import Field

class PhraseInput(BaseModel):

    author: str = "Anonim"  # name of the author
    text: str = Field(..., title= "text", description="text", max_length=100)


class PhraseOutput(PhraseInput):
    id: typing.Optional[int] = None  # phrase's id in database


class Database:
    # database is a dict

    def __init__(self):
        # id: model
        self._items: typing.Dict[int, PhraseOutput] = {}


    def get_random(self) -> int:
        return random.choice(self._items.keys())


    def get(self, id: int) -> typing.Optional[PhraseOutput]:
        return self._items.get(id)


    def add(self, phrase: PhraseInput) -> PhraseOutput:
        id = len(self._items) + 1
        phrase_out: PhraseOutput = PhraseOutput(id=id, **phrase.dict())
        self._items[phrase_out.id] = phrase_out
        return phrase_out

    def delete(self, id: int) -> typing.Union[typing.NoReturn, None]:
        if id in self._items:
            del self._items[id]
        else:
            raise ValueError("doesn't exist")

    