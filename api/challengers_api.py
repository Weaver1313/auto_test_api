from .base_api import BaseApi
import requests
from schemas.challengers_schema import scheme_response_body

class ChallengersApi(BaseApi):

    def __init__(self, challenger):
        super().__init__(challenger)


    def get_challengers(self):
        response = requests.get(f'{self.URL}/challenges',
                                headers=self.header)
        
        self.res_body = response.json()
        self.status = response.status_code


    def check_status_code_ok(self):
        assert self.status == 200


    def validate_response_body(self):
        validated = scheme_response_body(self.res_body)
        assert validated == self.res_body
        
