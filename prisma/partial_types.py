from prisma.models import Student, Note, Grade, StudentParticipates, StudentDisciplines

Student.create_partial('StudentRequest', exclude=['id', 'picture'], exclude_relational_fields=True)
Student.create_partial('StudentResponse', exclude_relational_fields=True, exclude=['StudentParticipates', 'StudentDisciplines'])

Note.create_partial('NoteRequest', exclude=['id', 'createdAt'], exclude_relational_fields=True)
Note.create_partial('NoteResponse', exclude_relational_fields=True)

Grade.create_partial('GradeRequest', exclude=['id'], exclude_relational_fields=True)
Grade.create_partial('GradeResponse', exclude_relational_fields=True)

StudentParticipates.create_partial('StudentParticipatesRequest', exclude=['id'], exclude_relational_fields=True)
StudentParticipates.create_partial('StudentParticipatesResponse', exclude_relational_fields=True)

StudentDisciplines.create_partial('StudentDisciplinesRequest', exclude=['id'], exclude_relational_fields=True)
StudentDisciplines.create_partial('StudentDisciplinesResponse', exclude_relational_fields=True)