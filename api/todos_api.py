from .base_api import BaseApi
import requests
from schemas import todos_schema


class TodosApi(BaseApi):

    def __init__(self, challenger):
        super().__init__(challenger)

    def get_todos(self):
        response = requests.get(f'{self.URL}/todos',
                                headers=self.header)
        
        self.status = response.status_code
        self.res_body = response.json()

    def check_status_code_ok(self):
        assert self.status == 200

    def validate_response_body(self):
        validate = todos_schema.schema_response_body(self.res_body)
        assert self.res_body == validate