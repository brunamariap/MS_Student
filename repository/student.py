from prisma.models import Student
from prisma.partials import StudentRequest

class StudentRepository:
  
  def __init__(self):
      self.repository = Student
      
  def create(self, request: StudentRequest):
    return self.repository.prisma().create(request)
		
  def get_all(self):
    return self.repository.prisma().find_many()
		
  def get_by_id(self):
    pass

  def change(self, id: str, request: StudentRequest):
    return self.repository.prisma().update(data=request, where={'id': id})
  
  def remove(self, id: str):
    return self.repository.prisma().delete({ 'id': id })