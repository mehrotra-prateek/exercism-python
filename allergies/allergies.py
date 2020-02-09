class Allergies(object):
    alrgens = {
            "eggs": 1,
            "peanuts": 2,
            "shellfish": 4,
            "strawberries": 8,
            "tomatoes": 16,
            "chocolate": 32,
            "pollen": 64,
            "cats": 128
            }

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return bool(self.score & self.alrgens.get(item, 0))

    @property
    def lst(self):
        return [alrgen for alrgen in self.alrgens if self.allergic_to(alrgen)]
