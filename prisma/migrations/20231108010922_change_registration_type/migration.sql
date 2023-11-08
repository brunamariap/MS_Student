/*
  Warnings:

  - You are about to alter the column `registration` on the `Student` table. The data in that column could be lost. The data in that column will be cast from `Int` to `BigInt`.

*/
-- RedefineTables
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_Student" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "registration" BIGINT NOT NULL,
    "dateOfBirth" DATETIME NOT NULL,
    "picture" TEXT NOT NULL,
    "classId" TEXT NOT NULL
);
INSERT INTO "new_Student" ("classId", "dateOfBirth", "id", "name", "picture", "registration") SELECT "classId", "dateOfBirth", "id", "name", "picture", "registration" FROM "Student";
DROP TABLE "Student";
ALTER TABLE "new_Student" RENAME TO "Student";
PRAGMA foreign_key_check;
PRAGMA foreign_keys=ON;
