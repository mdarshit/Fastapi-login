from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routes import auth


app = FastAPI(
    title = "Login system API",
    description = "A Login api built with FastAPI and Postgresql"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_headers = ["*"],
    allow_methods = ["*"]
)

app.include_router(auth.router)

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)

@app.get("/", summary = "Root endpoint")
async def root():
    """Welcome message for API"""
    return {"message": "Welcome to FastAPI login API"}