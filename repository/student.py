from prisma.models import Student
from prisma.partials import StudentRequest, StudentParticipatesRequest
from prisma.models import StudentParticipates


class StudentRepository:

    def __init__(self):
        self.repository = Student

    def create(self, request: StudentRequest):
        return self.repository.prisma().create(request)

    def get_all(self):
        return self.repository.prisma().find_many()

    def get_by_id(self, id: str):
        return self.repository.prisma().find_unique({'id': id})

    def create_student_link_to_event(self, request: StudentParticipatesRequest):
        return StudentParticipates.prisma().create(request)

    def get_event_participated(self, id: str):
        return StudentParticipates.prisma().find_many(where={'studentId': id})
    
    def remove_student_link_to_event(self, id: str):
        return StudentParticipates.prisma().delete({'id': id})

    def change(self, id: str, request: StudentRequest):
        return self.repository.prisma().update(data=request, where={'id': id})

    def remove(self, id: str):
        return self.repository.prisma().delete({'id': id})
