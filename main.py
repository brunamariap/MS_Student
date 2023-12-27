from fastapi import FastAPI, Depends
from prisma import Prisma
from controllers import student, note, grade

def is_authenticated():
    pass

app = FastAPI()
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