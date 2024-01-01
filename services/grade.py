from repository.grade import GradeRepository
from prisma.partials import GradeRequest
from typing import Optional, List
from services.discipline import DisciplineService

disciplineService = DisciplineService()

class GradeService:

    def __init__(self):
        self.repository = GradeRepository()

    def create(self, request: GradeRequest):
        return self.repository.create(request)
        

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id: str):
        return self.repository.get_by_id(id)

    def change(self, id: str, request: GradeRequest):
        return self.repository.change(id, request)

    def remove(self, id: str):
        return self.repository.remove(id)
    
    def get_student_grades(self, student_id: str, diary_id: str):
        student_grades = self.repository.get_student_grades(student_id, diary_id)

        grouped_data = {}
        for record in student_grades:
            discipline_id = record.disciplineId
            if discipline_id not in grouped_data:
                grouped_data[discipline_id] = []

            grouped_data[discipline_id].append(record)

        grades_with_disciplines = []
        for discipline_id, records in grouped_data.items():
            print(f"Discipline ID: {discipline_id}")
            discipline = disciplineService.get_discipline(discipline_id)
            discipline_with_grades = {
                **discipline,
                "grades": []
            }
            
            for record in records:
                new_record = {
                    **record.dict(),
                    'gradeId': record.id
                }
                del new_record['id']

                discipline_with_grades["grades"].append(new_record)
            grades_with_disciplines.append(discipline_with_grades)

        print(grades_with_disciplines)

        # for grade in student_grades:
        #     discipline = disciplineService.get_discipline(grade.disciplineId)
        #     grade_dict = {
        #         "diary_id": grade.diaryId,
        #         "attributed_by": grade.attributedBy,
        #         "bimester": grade.bimester,
        #         'discipline': discipline,
        #         "student_id": grade.studentId
        #     }
        #     grades_with_disciplines.append(grade_dict)
        
        return grades_with_disciplines
    
    def create_many_grades(self, request: List[GradeRequest]):
        return self.repository.create_many(request)
