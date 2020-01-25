import random
import string


class Robot:
    def __init__(self):
        random.seed()
        self.name = None
        self.reset()

    def reset(self):
        letters = random.choices(string.ascii_uppercase, k=2)
        numbers = random.choices(string.digits, k=3)
        self.name = ''.join(letters + numbers)
