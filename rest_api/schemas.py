from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class ChatRoomBase(BaseModel):
    name: str

class ChatRoomCreate(ChatRoomBase):
    pass

class ChatRoomOut(ChatRoomBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class MessageBase(BaseModel):
    content: Optional[str] = None
    media_url: Optional[str] = None

class MessageCreate(MessageBase):
    user_id: int
    room_id: int

class MessageOut(MessageBase):
    id: int
    user_id: int
    room_id: int
    created_at: datetime

    class Config:
        orm_mode = True 