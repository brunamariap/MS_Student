from prisma.models import Note
from prisma.partials import NoteRequest

class NoteRepository:
  
  def __init__(self):
      self.repository = Note
      
  def create(self, request: NoteRequest):
    return self.repository.prisma().create(request)
		
  def get_all(self):
    return self.repository.prisma().find_many()
		
  def get_by_id(self):
    pass

  def change(self, id: str, request: NoteRequest):
    return self.repository.prisma().update(data=request, where={'id': id})
  
  def remove(self, id: str):
    return self.repository.prisma().delete({ 'id': id })