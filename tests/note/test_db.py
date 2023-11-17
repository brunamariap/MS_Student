from fastapi.testclient import TestClient
from .test_base import TestBase
from main import app
from prisma.models import Note, Student
from .factories import NoteFactory
from ..student.factories import StudentFactory

client = TestClient(app)

class TestDB(TestBase):

    def test_get_all_notes(self, setUp):
        notes = Note.prisma().find_many()
        
        assert len(notes) >= 0

    def test_create_note(self, setUp):
        student_factory = StudentFactory()
        student = Student.prisma().create(student_factory.dict())

        factory = NoteFactory(student.id)
        note = Note.prisma().create(factory.dict())
        
        assert note
    
    def test_update_note(self, setUp):
        student_factory = StudentFactory()
        student = Student.prisma().create(student_factory.dict())

        factory = NoteFactory(student.id)
        note = Note.prisma().create(factory.dict())

        factory = NoteFactory(factory.studentId)

        updated_note = Note.prisma().update(
            data=factory.dict(),
            where={"id": note.id}
        )
        
        assert updated_note.title == factory.title
    
    def test_delete_note(self, setUp):
        student_factory = StudentFactory()
        student = Student.prisma().create(student_factory.dict())

        factory = NoteFactory(student.id)
        note = Note.prisma().create(factory.dict())

        deleted_note = Note.prisma().delete(
            where={"id": note.id}
        )
        
        assert deleted_note
