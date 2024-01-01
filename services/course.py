import requests
from fastapi import HTTPException, status


class CourseService: 

    def __init__(self, *args, **kwargs):
        # Academic Managament Microsservice
        self.baseUrl = 'http://127.0.0.1:8001'
    
    def get_course_details(self, course_id):
        response = requests.get(f'{self.baseUrl}/courses/{course_id}/details')

        if response.status_code != 200:
            raise HTTPException(status.HTTP_404_NOT_FOUND, {"details": "Não foi encontrado a disciplina com este ID"})
        
        return response.json()