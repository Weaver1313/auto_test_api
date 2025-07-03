from .base_api import BaseApi
import requests


class ChallengerApi(BaseApi):
    
    
    def __init__(self, challenger):
        super().__init__(challenger)
        

    def create_x_challenger(self):
        response = self.request('post', '/challenger', header={}, use_default_headers=False)
        # requests.post(f'{self.URL}/challenger')
        
        self.status = response.status_code
        self.x_challenger = response.headers
        

    def check_x_challenger(self): 
        assert 'X-Challenger' in self.x_challenger

