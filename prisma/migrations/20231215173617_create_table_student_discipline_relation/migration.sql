-- CreateTable
CREATE TABLE "StudentDisciplines" (
    "id" TEXT NOT NULL,
    "studentid" TEXT NOT NULL,
    "disciplineId" TEXT NOT NULL,

    CONSTRAINT "StudentDisciplines_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "StudentDisciplines" ADD CONSTRAINT "StudentDisciplines_studentid_fkey" FOREIGN KEY ("studentid") REFERENCES "Student"("id") ON DELETE CASCADE ON UPDATE CASCADE;
