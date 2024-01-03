from fastapi import FastAPI, Depends
from prisma import Prisma
from fastapi.middleware.cors import CORSMiddleware
from controllers import student, note, grade
from fastapi.staticfiles import StaticFiles

def is_authenticated():
    pass

app = FastAPI(title="MS Student")
app.mount("/static", StaticFiles(directory="static"), name="static")
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://localhost:8001",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student.router)
app.include_router(note.router)
app.include_router(grade.router)

prisma = Prisma(auto_register=True)

@app.on_event("startup")
def startup():
    prisma.connect()

@app.on_event("shutdown")
def shutdown():
    prisma.disconnect()