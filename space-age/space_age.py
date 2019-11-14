class SpaceAge(object):
    planet_year_ratio = {
                        'mercury': 0.2408467,
                        'venus': 0.61519726,
                        'earth': 1.0,
                        'mars': 1.8808158,
                        'jupiter': 11.862615,
                        'saturn': 29.447498,
                        'uranus': 84.016846,
                        'neptune': 164.79132
                        }
    earth_year = 31557600

    def __init__(self, seconds):
        self.earth_age = seconds/self.earth_year
        for planet in self.planet_year_ratio:
            setattr(self, "on_"+planet, self.planet_age(planet))

    def planet_age(self, planet):
        return lambda: round(self.earth_age/self.planet_year_ratio[planet], 2)
