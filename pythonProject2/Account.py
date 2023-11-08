from enum import Enum, IntEnum
from Constants import *

class Account:
    def __init__(self, id, password, user_role: UserRole):
        self.id = id
        self.password = password
        self.user_role = user_role

    def ComparePassword(self,password):
        return self.password == password
