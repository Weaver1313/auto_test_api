from .base_api import BaseApi
import requests
from schemas import todos_schema


class TodosApi(BaseApi):

    def __init__(self, challenger):
        super().__init__(challenger)


    def get_todos(self):
        return self.request('get', '/todos')


    def validate_response_body(self):
        self.validate_body(todos_schema.schema_response_body)

        