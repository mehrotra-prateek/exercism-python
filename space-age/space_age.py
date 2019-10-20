class SpaceAge(object):
    relative_year_ratio_for_planet={
                        'mercury': 0.2408467, 
                        'venus': 0.61519726, 
                        'earth': 1.0, 
                        'mars':1.8808158, 
                        'jupiter':11.862615, 
                        'saturn':29.447498, 
                        'uranus':84.016846,
                        'neptune':164.79132
                        }
    earth_year=31557600

    def __init__(self, seconds):
        self.age_on_earth=seconds/self.earth_year
        for planet in self.relative_year_ratio_for_planet:
            setattr(self, "on_"+planet, self.age_on_planet(planet))
            
    def age_on_planet(self, planet):        
        return lambda: round(self.age_on_earth/self.relative_year_ratio_for_planet[planet], 2)