
from datetime import datetime
from pydantic import BaseModel, Field, IPvAnyAddress, EmailStr

# Device schemas
class DeviceCreate(BaseModel):
    type: str = Field(..., max_length=30)
    model: str = Field(..., max_length=30)
    ip: IPvAnyAddress
    sn: str | None = Field(default=None, max_length=30)
    active: int = 0
    live: int = 0
    moniter: int = 0
    row_pos: int | None = None
    rack: int | None = None
    location: str | None = Field(default=None, max_length=255)
    lastcheck: datetime | None = None

class DeviceOut(BaseModel):
    id: int
    type: str
    model: str
    ip: str
    sn: str | None
    active: int
    live: int
    moniter: int
    row_pos: int | None
    rack: int | None
    location: str | None
    lastcheck: datetime | None
    created_date: datetime

    class Config:
        from_attributes = True

class DeviceUpdate(BaseModel):
    type: str | None = Field(default=None, max_length=30)
    model: str | None = Field(default=None, max_length=30)
    ip: IPvAnyAddress | None = None
    sn: str | None = Field(default=None, max_length=30)
    active: int | None = None
    live: int | None = None
    moniter: int | None = None
    row_pos: int | None = None
    rack: int | None = None
    location: str | None = Field(default=None, max_length=255)
    lastcheck: datetime | None = None

# Token schema
class Token(BaseModel):
    access_token: str
    token_type: str

# Users schemas
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=64)
    email: EmailStr | None = None
    password: str = Field(..., min_length=6)

class UserOut(BaseModel):
    id: int
    username: str
    email: str | None
    is_active: int
    is_admin: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
