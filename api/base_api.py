import json
import logging
import config
import requests



class BaseApi():
    
    def __init__(self, challenger):
        self.URL = config.URL
        self.status = None
        self.res_body = None
        self.header = {
                'X-CHALLENGER':challenger
            }
        

    def request(self, method,url_params, data=None, params=None, header=None ):
        url = f'{self.URL}{url_params}'
        merged_header = self.header.copy()

        if header:
            merged_header.update(header)

        try:
            response = requests.request(
                method=method.upper(),
                url=url,
                headers=merged_header,
                json=data,
                params=params,
                timeout=15

            )

            self.status = response.status_code

            try:
                self.res_body = response.json()

            except json.JSONDecodeError:
                self.res_body = response.text

            return response
            
        except requests.exceptions.RequestException as e:
            logging.error(f"HTTP request failed: {e}")
            self.status = None
            self.res_body = str(e)
            return None


    def validate_body(self, schema_func):
        validated = schema_func(self.res_body)
        assert validated == self.res_body
        
        
    def check_status_code(self, code):
        assert self.status == code