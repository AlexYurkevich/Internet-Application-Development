import requests
from base_class import *

class getId(BaseClient):

    BASE_URL = 'https://api.vk.com/method/'
    method = 'users.get'
    http_method = 'get'
    
    def __init__(self, username):
        self.parameters = (('user_ids', username), ('fields', 'bdate'))

    def get_params(self):
        return self.parameters

    def generate_url(self, method):
        return '{0}{1}'.format(self.BASE_URL, method)
    
    def _get_data(self, method, http_method):
        try:
            #response = requests[http_method](generate_url(method), params = self.get_params())
            response = requests.get(self.generate_url(method), params = self.get_params())
        except ConnectionError:
            print('Неудачная попытка отправки запроса')
        else:
            return self.response_handler(response) 

    def response_handler(self, response):
        return response

    def execute(self):
        return self._get_data(
            self.method,
            http_method=self.http_method
        )
