class PropertyListing:
    def __init__(self, titles=None, room_type=None, price_per_night=None, amenities=None, location=None):
        self.titles = titles
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.amenities = amenities or []
        self.location = location

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.titles}, {self.room_type}, "
                f"{self.price_per_night}, {self.amenities}, {self.location})")


class PropertyListingBuilder:
    def __init__(self):
        self.listing = PropertyListing()

    def set_titles(self, titles):
        self.listing.titles = titles
        return self

    def set_room_type(self, room_type):
        self.listing.room_type = room_type
        return self

    def set_price_per_night(self, price_per_night):
        self.listing.price_per_night = price_per_night
        return self

    def add_amenities(self, amenities):
        self.listing.amenities.append(amenities)
        return self

    def set_location(self, location):
        self.listing.location = location
        return self

    def build(self):
        return self.listing


def main() -> None:
    propertyListing: PropertyListing = (PropertyListingBuilder().set_titles("Cozy Cottage near beach").
                                        set_room_type("Entire Hom").set_price_per_night(200).add_amenities("WiFi").
                                        add_amenities("Air Conditioning").set_location("Malibu, California").build())

    print(propertyListing)


if __name__ == '__main__':
    main()
