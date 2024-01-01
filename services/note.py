from repository.note import NoteRepository
from prisma.partials import NoteRequest


class NoteService:

    def __init__(self):
        self.repository = NoteRepository()

    def create(self, request: NoteRequest):
        return self.repository.create(request)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id: str):
        return self.repository.get_by_id(id)

    def change(self, id: str, request: NoteRequest):
        return self.repository.change(id, request)

    def remove(self, id: str):
        return self.repository.remove(id)
    
    def get_student_notes(self, student_id: str):
        return self.repository.get_notes_by_student_id(student_id)