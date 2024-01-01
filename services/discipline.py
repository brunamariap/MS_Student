import requests
from fastapi import HTTPException, status
import os

class DisciplineService: 

    def __init__(self, *args, **kwargs):
        # Academic Managament Microsservice
        self.baseUrl = os.getenv("MS_ACADEMIC_MANAGEMENT_URL", 'http://127.0.0.1:8001')
    
    def get_discipline(self, discipline_id):
        response = requests.get(f'{self.baseUrl}/disciplines/{discipline_id}')

        if response.status_code != 200:
            raise HTTPException(status.HTTP_404_NOT_FOUND, {"details": "Não foi encontrado a disciplina com este ID"})
        
        return response.json()
    
    def get_discipline_details(self, discipline_id):
        response = requests.get(f'{self.baseUrl}/disciplines/{discipline_id}/details')

        if response.status_code != 200:
            raise HTTPException(status.HTTP_404_NOT_FOUND, {"details": "Não foi encontrado a disciplina com este ID"})
        
        return response.json()