-- CreateTable
CREATE TABLE "StudentParticipates" (
    "id" TEXT NOT NULL,
    "studentId" TEXT NOT NULL,
    "eventId" TEXT NOT NULL,

    CONSTRAINT "StudentParticipates_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "StudentParticipates" ADD CONSTRAINT "StudentParticipates_studentId_fkey" FOREIGN KEY ("studentId") REFERENCES "Student"("id") ON DELETE CASCADE ON UPDATE CASCADE;
