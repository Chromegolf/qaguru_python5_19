import random
from enum import Enum

BASE_URL = 'https://reqres.in/api/'
USER_EMAIL = 'eve.holt@reqres.in'
USER_PASSWORD = 'pistol'
USER_ID = random.randint(1, 10)

class JobList(str, Enum):
    leader = 'leader'
    manager = 'manager'
