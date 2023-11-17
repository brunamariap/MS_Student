from fastapi import APIRouter
from services.student import StudentRepository
from prisma.partials import StudentRequest, StudentResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from typing import List
from fastapi import status

router = APIRouter(prefix="/students", tags=['Estudante'])
studentRepository = StudentRepository()

@router.get("/all")
def list_students() -> List[StudentResponse]:
    response = studentRepository.get_all()
    
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.post("/create")
def insert_student(request: StudentRequest) -> StudentResponse:
    try:
        response = studentRepository.create(request.dict())

        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)

@router.put("/{id}/modify")
def modify_student(id: str, request: StudentRequest) -> StudentResponse:
    try:
        response = studentRepository.change(id, request.dict())

        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)

@router.delete("/remove")
def remove_student(id: str) -> StudentResponse:
    response = studentRepository.remove(id)
    
    if not response:
        return JSONResponse(content={"details": "Não foi encontrado um diário com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
    
    return JSONResponse(content={}, status_code=status.HTTP_204_NO_CONTENT)