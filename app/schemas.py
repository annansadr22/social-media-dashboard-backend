from pydantic import BaseModel
from typing import Optional
from typing_extensions import Literal
from datetime import datetime
from enum import Enum


# User Registration Request and Response Models
class UserRegister(BaseModel):
    name: str
    email: str
    password: str

class UserRegisterResponse(BaseModel):
    message: str

# User Login Request and Response Models
class UserLogin(BaseModel):
    email: str
    password: str

class UserLoginResponse(BaseModel):
    access_token: str
    token_type: str

# User Profile Models
class UserProfileUpdate(BaseModel):
    name: str
    bio: Optional[str] = None
    age: Optional[int] = None
    hobbies: Optional[str] = None

class UserProfileResponse(BaseModel):
    id: int
    name: str
    email: str
    bio: Optional[str] = None
    age: Optional[int] = None
    hobbies: Optional[str] = None
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True

# Admin Promotion Response Model
class AdminPromotionResponse(BaseModel):
    message: str


#For posting
class PostStatus(str, Enum):
    scheduled = "Scheduled"
    published = "Published"

class PostPlatform(str, Enum):
    facebook = "Facebook"
    instagram = "Instagram"
    linkedin = "LinkedIn"
    twitter = "Twitter"

class PostCreate(BaseModel):
    content: str
    platform: PostPlatform
    scheduled_time: Optional[datetime] = None
    status: PostStatus


class PostUpdate(BaseModel):
    content: Optional[str] = None
    platform: Optional[str] = None
    scheduled_time: Optional[datetime] = None
    status: Optional[str] = None

class PostResponse(BaseModel):
    id: int
    content: str
    platform: str
    scheduled_time: Optional[datetime]
    status: str
    user_id: int

    class Config:
        orm_mode = True

#Analysis
class PostAnalyticsResponse(BaseModel):
    post_id: int
    likes: int
    shares: int
    views: int

    class Config:
        orm_mode = True

#Filtering
class PostFilterRequest(BaseModel):
    content: Optional[str] = None
    platform: Optional[str] = None
    status: Optional[str] = None
    from_date: Optional[datetime] = None
    to_date: Optional[datetime] = None
    sort_order: Optional[Literal["asc", "desc"]] = "desc"

