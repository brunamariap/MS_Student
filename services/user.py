import requests
from fastapi import HTTPException, status
import os

class UserService: 

    def __init__(self, *args, **kwargs):
        # Authentication Microsservice
        self.baseUrl = os.getenv("MS_GATEWAY_URL", 'http://127.0.0.1:8000')
    
    def get_user_details(self, user_id):
        response = requests.get(f'{self.baseUrl}/users/{user_id}/details')
        
        if response.status_code != 200:
            raise HTTPException(status.HTTP_404_NOT_FOUND, {"details": "Não foi encontrado a disciplina com este ID"})
        
        return response.json()