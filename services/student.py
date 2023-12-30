from repository.student import StudentRepository
from prisma.partials import StudentRequest, StudentParticipatesRequest, StudentDisciplinesRequest
from typing import List
from services.discipline import DisciplineService

disciplineService = DisciplineService()

class StudentService:

    def __init__(self):
        self.service = StudentRepository()

    def create(self, request: StudentRequest):
        return self.service.create(request)

    def get_all(self):
        return self.service.get_all()

    def get_by_id(self, id: str):
        return self.service.get_by_id(id)

    def change(self, id: str, request: StudentRequest):
        return self.service.change(id, request)

    def remove(self, id: str):
        return self.service.remove(id)
    
    def get_all_student_and_events(self):
        return self.service.get_all_student_and_events()

    def create_student_link_to_event(self, request: List[StudentParticipatesRequest]):
        return self.service.create_student_link_to_event(request)

    def get_event_participated(self, id: str):
        return self.service.get_event_participated(id)
    
    def get_students_participated_event(self, eventId: str):
        return self.service.get_students_participated_event(eventId)
    
    def remove_student_link_to_event(self, id:str):
        return self.service.remove_student_link_to_event(id)
    
    def get_student_disciplines(self, student_id: str):
        student_disciplines = self.service.get_student_disciplines(student_id)
        
        disciplines = []
        for discipline in student_disciplines:
            discipline_details = disciplineService.get_discipline(discipline.disciplineId)
            disciplines.append(discipline_details) 
        
        return disciplines
    
    def create_link_student_discipline(self, request: List[StudentDisciplinesRequest]):
        return self.service.create_link_student_discipline(request)
    
    def remove_student_bond_discipline(self, id: str):
        return self.service.remove_student_bond_discipline(id)