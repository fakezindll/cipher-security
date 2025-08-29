from pydantic import BaseModel

class EncryptIn(BaseModel):
    text: str
    
class EncryptOut(BaseModel):
    token: str

class DecryptIn(BaseModel):
    token: str

class DecryptOut(BaseModel):
    text: str