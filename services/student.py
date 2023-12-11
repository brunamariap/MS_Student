from repository.student import StudentRepository
from prisma.partials import StudentRequest, StudentParticipatesRequest


class StudentService:

    def __init__(self):
        self.service = StudentRepository()

    def create(self, request: StudentRequest):
        return self.service.create(request)

    def get_all(self):
        return self.service.get_all()

    def get_by_id(self, id: str):
        return self.service.get_by_id(id)

    def create_student_link_to_event(self, request: StudentParticipatesRequest):
        return self.service.create_student_link_to_event(request)

    def get_event_participated(self, id: str):
        return self.service.get_event_participated(id)
    
    def remove_student_link_to_event(self, id: str):
        return self.service.create_student_link_to_event(id)

    def change(self, id: str, request: StudentRequest):
        return self.service.change(id, request)

    def remove(self, id: str):
        return self.service.remove(id)
