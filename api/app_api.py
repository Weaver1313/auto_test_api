from .challenger_api import ChallengerApi
from .challengers_api import ChallengersApi
from .todos_api import TodosApi
from .base_api import BaseApi

class App():
    

    def __init__(self, challenger):
        self.base_api = BaseApi(challenger)
        self.challenger_api = ChallengerApi(challenger)
        self.challengers_api = ChallengersApi(challenger)
        self.todos_api = TodosApi(challenger)
