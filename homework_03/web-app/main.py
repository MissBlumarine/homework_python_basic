from fastapi import FastAPI
from fastapi import HTTPException
from database import PhraseInput
from database import PhraseOutput
from database import Database

app = FastAPI()
db = Database()

@app.get("/ping/")
def root():
    return {"message": "pong"}


@app.get("/talk", response_description="Random phrase", description="Get random phrase from database", response_model=PhraseOutput)
async def get():
    try:
        phrase = db.get(db.get_random())
    except IndexError:
        raise HTTPException(404, "Phrase list is empty")
    return phrase


@app.post("/add", response_description="Added phrase with *id* parameter", response_model=PhraseOutput)
async def add(phrase: PhraseInput):
    phrase_out = db.add(phrase)
    return phrase_out

@app.delete("/delete", response_description="Result of deleting")
async def delete(id: int):
    try:
        db.delete(id)
    except ValueError as e:
        raise HTTPException(404, str(e))