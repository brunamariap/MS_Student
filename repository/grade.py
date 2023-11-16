from prisma.models import Grade
from prisma.partials import GradeRequest
from typing import Optional

class GradeRepository:

    def __init__(self):
        self.repository = Grade

    def create(self, request: GradeRequest):
        return self.repository.prisma().create(request)

    def get_all(self):
        return self.repository.prisma().find_many(include={'diary': True})

    def get_by_id(self, id):
        return self.repository.prisma().find_unique({'id': id})

    def change(self, id: str, request: GradeRequest):
        return self.repository.prisma().update(data=request, where={'id': id})

    def remove(self, id: str):
        return self.repository.prisma().delete({'id': id})

    def get_student_grades(self, student_id: str, diary_id: Optional[str]):
        if diary_id:
            return self.repository.prisma().find_many(
                where={
                    "studentId": student_id,
                    "diaryId": diary_id,
                }, 
                include={"diary": True },
            )

        return self.repository.prisma().find_many(where={
            "studentId": student_id
        }, include={'diary': True})