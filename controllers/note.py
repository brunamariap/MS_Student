from fastapi import APIRouter
from services.note import NoteService
from prisma.partials import NoteRequest, NoteResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List
from fastapi import status
from  prisma.errors import MissingRequiredValueError, ForeignKeyViolationError

router = APIRouter(prefix="/notes", tags=['Anotações'])
note_service = NoteService()

@router.get("/all")
def list_notes() -> List[NoteResponse]:
    response = note_service.get_all()
		
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.post("/create")
def insert_note(request: NoteRequest) -> NoteResponse:
    try:
        response = note_service.create(request.dict())

        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)