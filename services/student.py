from repository.student import StudentRepository
from prisma.partials import StudentRequest

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
