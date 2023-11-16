from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from .test_base import TestBase
from main import app
from prisma.models import Student
from prisma.partials import StudentRequest
from .factories import StudentFactory

client = TestClient(app)

class TestApp(TestBase):

    def test_get_all_students(self, setUp):
        factory = StudentFactory('1123')

        students = Student.prisma().create(StudentRequest(**factory))
        
        assert students
