from repository.note import NoteRepository
from prisma.partials import NoteRequest


class NoteService:

    def __init__(self):
        self.service = NoteRepository()

    def create(self, request: NoteRequest):
        return self.service.create(request)

    def get_all(self):
        return self.service.get_all()

    def get_by_id(self, id: str):
        return self.service.get_by_id(id)

    def change(self, id: str, request: NoteRequest):
        return self.service.change(id, request)

    def remove(self, id: str):
        return self.service.remove(id)
