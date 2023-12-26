from fastapi import APIRouter
from services.student import StudentService
from prisma.partials import StudentRequest, StudentResponse, StudentParticipatesRequest, StudentParticipatesResponse, StudentDisciplinesRequest, StudentDisciplinesResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from typing import List
from fastapi import status
import requests

router = APIRouter(prefix="/students", tags=['Estudante'])
student_service = StudentService()

academic_management_MS_url_base = 'http://127.0.0.1:8001'

def check_if_discipline_exists(disciplineId:str):
    try:
        url = f"{academic_management_MS_url_base}/disciplines/{disciplineId}/details"
        response = requests.get(url)

        if response.status_code == 200:
            return True
        elif not response:
            return JSONResponse(content={"details": "Não foi encontrado uma disciplina com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)

    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/all")
def list_students() -> List[StudentResponse]:
    response = student_service.get_all()

    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)


@router.post("/create")
def insert_student(request: StudentRequest) -> StudentResponse:
    try:
        url = f"{academic_management_MS_url_base}/classes/{request.dict()['classId']}/details"
        response = requests.get(url=url)
        if response.status_code == 200:
            response = student_service.create(request.dict())

            return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_201_CREATED)
        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_400_BAD_REQUEST)
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
        url = f"{academic_management_MS_url_base}/classes/{request.dict()['classId']}/details"
        response = requests.get(url=url)
        if response.status_code == 200:
            response = student_service.change(id, request.dict())

            return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)


@router.delete("/remove")
def remove_student(id: str) -> StudentResponse:
    try:
        response = student_service.remove(id)

        if not response:
            return JSONResponse(content={"details": "Não foi encontrado um estudante com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)

        return JSONResponse(content={}, status_code=status.HTTP_204_NO_CONTENT)

    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/{id}/events/all")
def get_student_event_participated(id: str) -> List[StudentParticipatesResponse]:
    try:
        response = student_service.get_event_participated(id)

        if not response:
            return JSONResponse(content={"details": "Não foi encontrado estudante com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)

        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)
    


@router.delete("/{id}/events/remove")
def remove_student_link_to_event(id: str):
    try:
        response = student_service.remove_student_link_to_event(id)

        if not response:
            return JSONResponse(content={"details": "Não foi encontrado um estudante com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)

        return JSONResponse(content={}, status_code=status.HTTP_204_NO_CONTENT)

    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)


@router.post("/events/link")
def link_students_to_events(request: List[StudentParticipatesRequest]) -> List[StudentParticipatesRequest]:
    try:
        formated_request = []
        for item in request:
            formated_request.append(item.dict())
        response = student_service.create_student_link_to_event(
            formated_request)

        return JSONResponse(content=jsonable_encoder(formated_request), status_code=status.HTTP_201_CREATED)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/events/links/all")
def get_all_student_and_events():
    try:
        response = student_service.get_all_student_and_events()

        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/{id}/disciplines/all")
def get_student_disciplines(id: str):
    try:
        response = student_service.get_student_disciplines(id)

        if not response:
            return JSONResponse(content={"details": "Não foi encontrado um estudante com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)

        return JSONResponse(content={}, status_code=status.HTTP_204_NO_CONTENT)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)


@router.post("/{id}/disciplines/create")
def create_link_student_discipline(id: str, request: List[StudentDisciplinesRequest]):
    try:
        formated_request = []
        for item in request:
            data = item.dict()
            formated_request.append(data)
            # print(data["disciplineId"])
            # response = check_if_discipline_exists(data['disciplineId'])

            # if response != True:
            #     print('entrou')
            #     return response

        response = student_service.create_link_student_discipline(
            formated_request)

        return JSONResponse(content=jsonable_encoder(formated_request), status_code=status.HTTP_201_CREATED)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)


@router.delete("/disciplines/{id}/remove")
def remove_student_bond_discipline(id: str):
    try:
        response = student_service.remove_student_bond_discipline(id)

        if not response:
            return JSONResponse(content={"details": "Não foi encontrado um estudante com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)

        return JSONResponse(content={}, status_code=status.HTTP_204_NO_CONTENT)

    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)