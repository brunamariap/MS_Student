from repository.note import NoteRepository
from prisma.partials import NoteRequest
from services.user import UserService


userService = UserService()
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

        student_notes = self.repository.get_notes_by_student_id(student_id)
        notes = []
        for note in student_notes:
            user = userService.get_user_details(note.createdBy)
            notes.append({
                **note.dict(),
                "user": user
            })
            
        return notes