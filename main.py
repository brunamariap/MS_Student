from fastapi import FastAPI
from prisma import Prisma
from controllers import student, note, grade

app = FastAPI()
app.include_router(student.router)
app.include_router(note.router)
app.include_router(grade.router)

prisma = Prisma(auto_register=True)

@app.on_event("startup")
async def startup():
    await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()