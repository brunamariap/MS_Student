from prisma.models import Student, Note, Grade

Student.create_partial('StudentRequest', exclude=['id'], exclude_relational_fields=True)
Student.create_partial('StudentResponse', exclude_relational_fields=True)

Note.create_partial('NoteRequest', exclude=['id'], exclude_relational_fields=True)
Note.create_partial('NoteResponse', exclude_relational_fields=True)

Grade.create_partial('GradeRequest', exclude=['id'], exclude_relational_fields=True)
Grade.create_partial('GradeResponse', exclude_relational_fields=True)