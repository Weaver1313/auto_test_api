from .base_api import BaseApi
import requests
from schemas.challengers_schema import scheme_response_body

class ChallengersApi(BaseApi):

    def __init__(self, challenger):
        super().__init__(challenger)


    def get_challengers(self):
        return self.request('get', '/challenges')


    def validate_response_body(self):
        self.validate_body(scheme_response_body)
        
        
