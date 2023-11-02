from fastapi import APIRouter
from services.student import StudentRepository
from prisma.partials import StudentRequest, StudentResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List
from fastapi import status

router = APIRouter(prefix="/students", tags=['Estudante'])
studentRepository = StudentRepository()

@router.get("/all")
async def list_students() -> List[StudentResponse]:
    response = await studentRepository.get_all()
		
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.post("/create")
async def insert_student(request: StudentRequest) -> StudentResponse:
    response = await studentRepository.create(request.dict())
		
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.put("/{id}/modify")
async def modify_student(id: str, request: StudentRequest) -> StudentResponse:
    response = await studentRepository.change(id, request.dict())
		
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.delete("/remove")
async def remove_student(id: str) -> StudentResponse:
    response = await studentRepository.remove(id)
    
    if not response:
        return JSONResponse(content={"details": "Não foi encontrado um diário com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
    
    return JSONResponse(content={}, status_code=status.HTTP_204_NO_CONTENT)