from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from .test_base import TestBase
from main import app
from prisma.models import Student
from .factories import StudentFactory

client = TestClient(app)

class TestDB(TestBase):

    def test_get_all_students(self, setUp):
        students = Student.prisma().find_many()
        
        assert len(students) >= 0

    def test_create_student(self, setUp):
        factory = StudentFactory()
        student = Student.prisma().create(factory.dict())
        
        assert student
    
    def test_update_student(self, setUp):
        factory = StudentFactory()
        student = Student.prisma().create(factory.dict())

        factory = StudentFactory()

        updated_student = Student.prisma().update(
            data=factory.dict(),
            where={"id": student.id}
        )
        
        assert updated_student.name == factory.name
    
    def test_delete_student(self, setUp):
        factory = StudentFactory()
        student = Student.prisma().create(factory.dict())

        deleted_student = Student.prisma().delete(
            where={"id": student.id}
        )
        
        assert deleted_student