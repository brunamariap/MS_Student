/*
  Warnings:

  - You are about to drop the column `studentid` on the `StudentDisciplines` table. All the data in the column will be lost.
  - Added the required column `studentId` to the `StudentDisciplines` table without a default value. This is not possible if the table is not empty.

*/
-- DropForeignKey
ALTER TABLE "StudentDisciplines" DROP CONSTRAINT "StudentDisciplines_studentid_fkey";

-- AlterTable
ALTER TABLE "StudentDisciplines" DROP COLUMN "studentid",
ADD COLUMN     "studentId" TEXT NOT NULL;

-- AddForeignKey
ALTER TABLE "StudentDisciplines" ADD CONSTRAINT "StudentDisciplines_studentId_fkey" FOREIGN KEY ("studentId") REFERENCES "Student"("id") ON DELETE CASCADE ON UPDATE CASCADE;
