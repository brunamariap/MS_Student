from fastapi import APIRouter
from services.grade import GradeService
from prisma.partials import GradeRequest, GradeResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List, Optional
from fastapi import status

router = APIRouter(prefix="/grades", tags=['Grades'])
gradeService = GradeService()


@router.get("/all")
def list_grades() -> List[GradeResponse]:
    response = gradeService.get_all()

    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)


@router.get("/{student_id}")
def get_student_grades(student_id: str, diary_id: Optional[str] = None) -> List[GradeResponse]:
    response = gradeService.get_student_grades(student_id, diary_id)
    if not response:
        return JSONResponse(content={"details": "Não foi encontrado notas com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)


@router.get("/{id}/details")
def get_grade(id: str) -> List[GradeResponse]:
    try:
        response = gradeService.get_by_id(id)
        if not response:
            return JSONResponse(content={"details": "Não foi encontrado notas com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)


@router.post("/create")
def insert_grade(request: GradeRequest) -> GradeResponse:
    try:
        body: GradeRequest = request
        response = gradeService.create(body.dict())

        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)


@router.put("/{id}/modify")
def change_grade(id: str, request: GradeRequest) -> GradeResponse:
    try:
        body: GradeRequest = request
        response = gradeService.change(id, request.dict())

        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)


@router.delete("/remove")
def remove_grade(id: str) -> None:
    response = gradeService.remove(id)

    if not response:
        return JSONResponse(content={"details": "Não foi encontrado notas com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(content=None, status_code=status.HTTP_204_NO_CONTENT)
