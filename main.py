from fastapi import FastAPI, HTTPException, Request, status, Depends
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import BaseModel, RequestValidationError
import router_example
from router_example import CreateUser
import json
from sqlalchemy.orm import Session
from sql_example.database import Base, engine, SessionLocal, User
from nosql_example.database import user_collection, collection


app = FastAPI()
app.include_router(router_example.router)



@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
        "message": "Oops! Something went wrong"
        
        },
        )





@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/error_endpoint")
async def raise_exception():
    raise HTTPException(status_code=404)



Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()

    try: 
        yield db
    finally: 
        db.close()


@app.post('/new-users')
def get_all_users(request: CreateUser, db: Session = Depends(get_db)):
    new_user = User(
        name = request.name,
        email = request.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/user')
def get_users(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User Does Not Exist")
    return user



@app.patch('/user/{user_id}')
def get_users(user_id: int, request: CreateUser, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User Does Not Exist")
    user.email = request.email
    user.name = request.name
    db.commit()
    db.refresh(user)
    return user


@app.post('/user/{user_id}')
def del_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User Does Not Exist")
    
    db.delete(user)
    db.commit()
    
    return {"message": "User Deleted"}


@app.get('/users')
def get_all_users() -> list[CreateUser]:
    

    return  [user for user in collection.find()]


