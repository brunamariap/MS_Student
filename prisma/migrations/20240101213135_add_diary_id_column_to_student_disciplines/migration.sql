/*
  Warnings:

  - Added the required column `diaryId` to the `StudentDisciplines` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "StudentDisciplines" ADD COLUMN     "diaryId" TEXT NOT NULL;
