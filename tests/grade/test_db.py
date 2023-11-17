from fastapi.testclient import TestClient
from .test_base import TestBase
from main import app
from prisma.models import Grade, Student
from .factories import GradeFactory
from ..student.factories import StudentFactory

client = TestClient(app)

class TestDB(TestBase):

    def test_get_all_grades(self, setUp):
        notes = Grade.prisma().find_many()
        
        assert len(notes) >= 0

    def test_create_grade(self, setUp):
        student_factory = StudentFactory()
        student = Student.prisma().create(student_factory.dict())

        factory = GradeFactory(student.id)
        note = Grade.prisma().create(factory.dict())
        
        assert note
    
    def test_update_grade(self, setUp):
        student_factory = StudentFactory()
        student = Student.prisma().create(student_factory.dict())

        factory = GradeFactory(student.id)
        note = Grade.prisma().create(factory.dict())

        factory = GradeFactory(factory.studentId)

        updated_note = Grade.prisma().update(
            data=factory.dict(),
            where={"id": note.id}
        )
        
        assert updated_note.score == factory.score
    
    def test_delete_grade(self, setUp):
        student_factory = StudentFactory()
        student = Student.prisma().create(student_factory.dict())

        factory = GradeFactory(student.id)
        note = Grade.prisma().create(factory.dict())

        deleted_note = Grade.prisma().delete(
            where={"id": note.id}
        )
        
        assert deleted_note
