from fastapi import APIRouter
from services.student import StudentService
from prisma.partials import StudentRequest, StudentResponse, StudentParticipatesRequest, StudentParticipatesResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from typing import List
from fastapi import status

router = APIRouter(prefix="/students", tags=['Estudante'])
student_service = StudentService()

@router.get("/all")
def list_students() -> List[StudentResponse]:
    response = student_service.get_all()
    
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.post("/create")
def insert_student(request: StudentRequest) -> StudentResponse:
    try:
        response = student_service.create(request.dict())

        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_201_CREATED)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)

@router.get("/{id}/details")
def get_student(id: str) -> List[StudentResponse]:
    try:
        response = student_service.get_by_id(id)

        if not response:
            return JSONResponse(content={"details": "Não foi encontrado estudante com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)

@router.put("/{id}/modify")
def modify_student(id: str, request: StudentRequest) -> StudentResponse:
    try:
        response = student_service.change(id, request.dict())

        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)

@router.delete("/remove")
def remove_student(id: str) -> StudentResponse:
    try:
        response = student_service.remove(id)
        
        if not response:
            return JSONResponse(content={"details": "Não foi encontrado um diário com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
        
        return JSONResponse(content={}, status_code=status.HTTP_204_NO_CONTENT)

    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)
    

@router.get("/{id}/events/all")
def get_student_event_participated(id: str) -> List[StudentResponse]:
    try:
        response = student_service.get_event_participated(id)

        if not response:
            return JSONResponse(content={"details": "Não foi encontrado estudante com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)

        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)

# @router.post("/{id}/events/create")
# def insert_link_student_to_event(request: StudentParticipatesRequest) -> List[StudentParticipatesResponse]:
#     try:
#         response = student_service.create_student_link_to_event(request.dict())

#         return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_201_CREATED)

#     except Exception as error:
#         return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)
