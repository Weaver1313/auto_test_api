from .base_api import BaseApi
import requests
from schemas import todos_schema
import pytest


class TodosApi(BaseApi):

    def __init__(self, challenger):
        super().__init__(challenger)

    def get_todos(self, path):
        return self.request('get', path)
        
    def validate_response_body(self):
        self.validate_body(todos_schema.schema_response_body)


    def create_todos(self, path):
        response = self.request('post', path, 
                                data={
                                    "title": "create todo process payroll",
                                    "doneStatus": True,
                                    "description": ""
                                })
        print(response.json())


    def validate_res_body_create(self):
        self.validate_body(todos_schema.schema_create_todos)
        