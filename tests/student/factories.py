from prisma.partials import StudentRequest
from datetime import datetime
from faker import Faker
from random import randint
import uuid

fake = Faker('pt-BR')

class StudentFactory():

    def __init__(self):
        self.name = fake.name()
        self.registration = randint(2023094040000, 2023094049999)
        self.dateOfBirth = fake.date_time()
        self.picture = fake.image_url()
        self.classId = str(uuid.uuid4())

    def dict(self):
        return {
            "name": self.name,
            "registration": self.registration,
            "dateOfBirth": self.dateOfBirth.isoformat() + 'Z',
            "picture": self.picture,
            "classId": self.classId,
        }

class StudentParticipatesFactory:
    
    def __init__(self) :
        pass