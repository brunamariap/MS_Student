from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from prisma.partials import StudentRequest
from .test_base import TestBase
from main import app
from .factories import StudentFactory
from prisma.models import Student

client = TestClient(app)
prefix = "/students"

class TestRoutes(TestBase):

    def test_get_student(self, setUp):
        factory = StudentFactory()
        student = Student.prisma().create(factory.dict())

        response = client.get(
            f"{prefix}/{student.id}/details")
        assert response.status_code == 200

    def test_get_student_event_participated(self, setUp):
        factory = StudentFactory()
        student = Student.prisma().create(factory.dict())

        response = client.get(
            f"{prefix}/{student.id}/events/all")
        assert response.status_code == 200

