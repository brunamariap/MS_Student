from repository.student import StudentRepository
from prisma.partials import StudentRequest, StudentParticipatesRequest, StudentDisciplinesRequest
from typing import List
from services.discipline import DisciplineService
from services.event import EventService
from services.school_class import ClassService
from services.grade import GradeService
from fastapi import Path, UploadFile
from typing import Optional
import uuid
import shutil
import os

disciplineService = DisciplineService()
eventService = EventService()
classService = ClassService()
gradeService = GradeService()

class StudentService:

    def __init__(self):
        self.repository = StudentRepository()

    def create(self, request: StudentRequest):
        return self.repository.create(request)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id: str):
        student = self.repository.get_by_id(id)
        student_class = classService.get_class_details(student.classId)
        student_with_details = {
            **student.dict(),
            "schoolClass": student_class
        }
        
        return student_with_details

    def change(self, id: str, request: StudentRequest):
        return self.repository.change(id, request)

    def remove(self, id: str):
        return self.repository.remove(id)
    
    def get_all_student_and_events(self):
        return self.repository.get_all_student_and_events()

    def create_student_link_to_event(self, request: List[StudentParticipatesRequest]):
        return self.repository.create_student_link_to_event(request)

    def get_event_participated(self, student_id: str):
        event_participations = self.repository.get_event_participated(student_id)
        
        events = []
        for event in event_participations:
            response = eventService.get_event_details(event.eventId)
            events.append(response)

        return events
    
    def get_students_participated_event(self, eventId: str):
        return self.repository.get_students_participated_event(eventId)
    
    def remove_student_link_to_event(self, id:str):
        return self.repository.remove_student_link_to_event(id)
    
    def get_student_disciplines(self, student_id: str):
        student_disciplines = self.repository.get_student_disciplines(student_id)
        
        disciplines = []
        for discipline in student_disciplines:
            discipline_details = disciplineService.get_discipline(discipline.disciplineId)
            disciplines.append(discipline_details) 
        
        return disciplines
    
    def create_link_student_discipline(self, request: List[StudentDisciplinesRequest]):
        response = self.repository.create_link_student_discipline(request)

        return response
    
    def remove_student_bond_discipline(self, id: str):
        return self.repository.remove_student_bond_discipline(id)
    
    def change_student_picture(self, student_id: str, picture: UploadFile):
        student = self.repository.get_by_id(student_id)
        
        picture.filename = f"{uuid.uuid4()}.jpg"
        upload_folder = "./static/pictures"
        os.makedirs(upload_folder, exist_ok=True)

        file_path = os.path.join(upload_folder, picture.filename)

        with open(file_path, "wb") as image:
            shutil.copyfileobj(picture.file, image)

        return self.repository.change(student_id, picture)