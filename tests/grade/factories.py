from faker import Faker
from random import randint
import uuid
fake = Faker('pt-BR')

class GradeFactory():

    def __init__(self, studentId):
        self.score = randint(0, 100)
        self.bimester = randint(1, 4)
        self.studentId = studentId
        self.diaryId = str(uuid.uuid4())
        self.disciplineId = str(uuid.uuid4())
        self.attributedBy = str(uuid.uuid4())

    def dict(self):
        return {
            "score": self.score,
            "bimester": self.bimester,
            "disciplineId": self.disciplineId,
            "studentId": self.studentId,
            "diaryId": self.diaryId,
            "attributedBy": self.attributedBy,
        }