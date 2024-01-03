from prisma.models import Student, StudentParticipates, StudentDisciplines
from prisma.partials import StudentRequest, StudentParticipatesRequest, StudentDisciplinesRequest
from typing import List
from fastapi import UploadFile

class StudentRepository:

    def __init__(self):
        self.repository = Student

    def create(self, request: StudentRequest):
        return self.repository.prisma().create(request)

    def get_all(self):
        return self.repository.prisma().find_many()

    def get_by_id(self, id: str):
        return self.repository.prisma().find_unique({ 'id': id })

    def change(self, id: str, request: StudentRequest):
        return self.repository.prisma().update(data=request, where={'id': id})
    
    def change_picture(self, id: str, picture: UploadFile):
        return self.repository.prisma().update(data={'picture': picture.filename}, where={'id': id})

    def remove(self, id: str):
        return self.repository.prisma().delete({'id': id})
    
    def get_all_student_and_events(self):
        return StudentParticipates.prisma().find_many(include={'student': True})

    def get_event_participated(self, student_id: str):
        return StudentParticipates.prisma().find_many(where={'studentId': student_id})
    
    def get_students_participated_event(self, eventId: str):
        return StudentParticipates.prisma().find_many({'eventId': eventId})
    
    def create_student_link_to_event(self, request: List[StudentParticipatesRequest]):
        return StudentParticipates.prisma().create_many(request, skip_duplicates=True)
    
    def remove_student_link_to_event(self, id: str):
        return StudentParticipates.prisma().delete({'id': id})

    def get_student_disciplines(self, studentId: str):
        return StudentDisciplines.prisma().find_many(where={'studentId': studentId})
    
    def create_link_student_discipline(self, request: List[StudentDisciplinesRequest]):
        return StudentDisciplines.prisma().create_many(request, skip_duplicates=True)
    
    def remove_student_bond_discipline(self, id: str):
        return StudentDisciplines.prisma().delete({'id': id})