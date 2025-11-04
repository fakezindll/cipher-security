from pydantic import BaseModel

class EncryptIn(BaseModel):
    text: str
    key: str  # nova chave personalizada

class EncryptOut(BaseModel):
    token: str

class DecryptIn(BaseModel):
    token: str
    key: str  # nova chave personalizada

class DecryptOut(BaseModel):
    text: str
