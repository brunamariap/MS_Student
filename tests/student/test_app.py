from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from .test_base import TestBase
from main import app
from prisma.models import Student
client = TestClient(app)

class TestApp(TestBase):

    def test_get_all_students(self, setUp):
        students = Student.prisma().find_many()

        assert len(students) == 0
