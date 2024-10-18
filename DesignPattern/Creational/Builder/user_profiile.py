class userProfileBuilder:
    def __init__(self):
        self.profile = {}

    def set_name(self, name):
        self.profile['name'] = name
        return self

    def set_age(self, age):
        self.profile['age'] = age
        return self

    def set_bio(self, bio):
        self.profile['bio'] = bio
        return self

    def set_photo(self, photo_url):
        self.profile['photo'] = photo_url
        return self

    def set_connections(self, connections):
        self.profile['connections'] = connections
        return self

    def build(self):
        return self.profile
