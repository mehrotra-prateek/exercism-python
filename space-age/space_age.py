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
        self.age_on_planet=seconds/self.earth_year

    def on_mercury(self):
        return(round(self.age_on_planet/self.relative_year_ratio_for_planet['mercury'], 2))

    def on_venus(self):
        return(round(self.age_on_planet/self.relative_year_ratio_for_planet['venus'], 2))    
    
    def on_earth(self):
        return(round (self.age_on_planet/self.relative_year_ratio_for_planet['earth'], 2))

    def on_mars(self):
        return(round(self.age_on_planet/self.relative_year_ratio_for_planet['mars'], 2))

    def on_jupiter(self):
        return(round(self.age_on_planet/self.relative_year_ratio_for_planet['jupiter'], 2))    

    def on_saturn(self):
        return(round(self.age_on_planet/self.relative_year_ratio_for_planet['saturn'], 2))

    def on_uranus(self):
        return(round(self.age_on_planet/self.relative_year_ratio_for_planet['uranus'], 2))    

    def on_neptune(self):
        return(round(self.age_on_planet/self.relative_year_ratio_for_planet['neptune'], 2))