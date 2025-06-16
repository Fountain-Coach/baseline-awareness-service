from pydantic import BaseModel

class InitIn(BaseModel):
    corpusId: str

class InitOut(BaseModel):
    message: str
