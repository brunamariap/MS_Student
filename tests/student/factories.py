from prisma.partials import StudentRequest
from datetime import datetime

class StudentFactory():

    def __init__(self, classId):
        self.name ="aleatorio"
        self.registration = 200
        self.dateOfBirth = datetime.utcnow().isoformat()
        self.picture ="aleatorio"
        self.classId = classId


    
    
