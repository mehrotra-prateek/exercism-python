class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds=seconds
        self.age=((((self.seconds/60)/60)/24)/365.25)
        pass

    def on_earth(self,age_on_earth=0):
        return(round(self.age, 2))

    def on_mercury(self, age_on_mercury=0):
        return(round(self.age/0.2408467, 2))

    def on_venus(self, age_on_venus=0):
        return(round(self.age/0.61519726, 2))    
    
    def on_mars(self, age_on_mars=0):
        return(round(self.age/1.8808158, 2))

    def on_jupiter(self, age_on_jupiter=0):
        return(round(self.age/11.862615, 2))    

    def on_saturn(self, age_on_saturn=0):
        return(round(self.age/29.447498, 2))

    def on_uranus(self, age_on_uranus=0):
        return(round(self.age/84.016846, 2))    

    def on_neptune(self, age_on_neptune=0):
        return(round(self.age/164.79132, 2))    

