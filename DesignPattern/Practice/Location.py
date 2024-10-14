class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"{self.__class__.__name__}({self.latitude}, {self.longitude})"
