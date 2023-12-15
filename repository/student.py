from prisma.models import Student
from prisma.partials import StudentRequest, StudentParticipatesRequest
from prisma.models import StudentParticipates
from typing import List


class StudentRepository:

    def __init__(self):
        self.repository = Student

    def create(self, request: StudentRequest):
        return self.repository.prisma().create(request)

    def get_all(self):
        return self.repository.prisma().find_many()

    def get_by_id(self, id: str):
        return self.repository.prisma().find_unique({'id': id})

    def create_student_link_to_event(self, request: List[StudentParticipatesRequest]):
        return StudentParticipates.prisma().create_many(request, skip_duplicates=True)

    def get_event_participated(self, id: str):
        return StudentParticipates.prisma().find_many(where={'studentId': id})
    
    def get_students_participated_event(self, eventId: str):
        return StudentParticipates.prisma().find_many(where={'eventId': eventId})
    
    def remove_student_link_to_event(self, id: str):
        return StudentParticipates.prisma().delete({'id': id})
        # return StudentParticipates.prisma().delete_many(where={'studentId': '7e5fd67a-926d-42d3-b740-a3d725728770'})

    def change(self, id: str, request: StudentRequest):
        return self.repository.prisma().update(data=request, where={'id': 'id'})

    def remove(self, id: str):
        return self.repository.prisma().delete({'id': id})
