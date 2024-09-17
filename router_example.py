from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional, Annotated


router = APIRouter()


class Book(BaseModel):
    title: str
    author: str
    year: int

class Tweet(BaseModel):
    content: str
    hashtags: list[str]



class CreateUser(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int]
    tweets: list[Tweet] | None = None
    @field_validator('age')
    def validate_age(cls, value):
        if value < 18 or value > 100:
            raise ValueError(
                "Age Must be between 18 and 100"
            )
        return value

class BookResponse(BaseModel):
    title: str
    author: str


@router.post('/addbook')
async def add_book(book: Book, idn: int = 77, ugo: str = "Hello"):
    return {
        "message": "Account Created",
        "book_info": book,
        "idn": idn,
        "ugo": ugo

    }


@router.get('/allbook', response_model=list[BookResponse])
async def add_book():
    return  [
             {
             "id": 1,
             "title": "1984",
             "author": "George Orwell"},
             {
             "id": 1,
             "title": "The Great Gatsby",
             "author": "F. Scott Fitzgerald",
             },
             ]

