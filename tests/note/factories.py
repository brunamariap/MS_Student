from faker import Faker
from random import randint
import uuid
fake = Faker('pt-BR')

class NoteFactory():

    def __init__(self, studentId):
        self.title = fake.text(max_nb_chars=20)
        self.description = fake.paragraph(nb_sentences=4)
        self.createdBy = str(uuid.uuid4())
        self.studentId = studentId

    def dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "createdBy": self.createdBy,
            "studentId": self.studentId,
        }