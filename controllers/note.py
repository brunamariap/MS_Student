from fastapi import APIRouter
from services.note import NoteRepository
from prisma.partials import NoteRequest, NoteResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List
from fastapi import status

router = APIRouter(prefix="/notes", tags=['Anotações'])
noteRepository = NoteRepository()

@router.get("/all")
async def list_notes() -> List[NoteResponse]:
    response = await noteRepository.get_all()
		
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.post("/create")
async def insert_note(request: NoteRequest) -> NoteResponse:
    response = await noteRepository.create(request.dict())
		
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)