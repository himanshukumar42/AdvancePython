from Uber import VehicleFactory, Vehicle  # Factory Design Pattern
from Payment import PaymentGateway, PaymentGatewayFactory
from Location import Location
from copy import deepcopy


class RideRequest:
    def __init__(self, vehicle_type: str = "", payment_method: str = None, pickup_location: Location = None,
                 drop_location: Location = None, arrival_time=None, features=None):
        self.vehicle_type = vehicle_type
        self.pickup_location = pickup_location
        self.drop_location = drop_location
        self.arrival_time = arrival_time
        self.features = features or []
        self.payment_method = payment_method

    def clone(self):  # Prototype Design Pattern
        return deepcopy(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.pickup_location}, {self.drop_location}, {self.vehicle_type}, {self.payment_method}, {self.arrival_time}, {self.features})"


# Builder Design Pattern
class RideRequestBuilder:
    def __init__(self):
        self.ride_request = RideRequest()

    def set_pickup_location(self, pickup: Location):
        self.ride_request.pickup_location = pickup
        return self

    def set_drop_location(self, drop: Location):
        self.ride_request.drop_location = drop
        return self

    def set_vehicle_type(self, vehicle_type: Vehicle):
        self.ride_request.vehicle_type = vehicle_type
        return self

    def set_payment_method(self, payment_method: PaymentGateway):
        self.ride_request.payment_method = payment_method
        return self

    def set_arrival_time(self, arrival_time):
        self.ride_request.arrival_time = arrival_time
        return self

    def add_features(self, feature):
        self.ride_request.features.append(feature)
        return self

    def build(self):
        return self.ride_request


def main() -> None:
    vehicle_object = VehicleFactory.create_vehicle_ride("BookAny")
    new_vehicle_object = vehicle_object.clone()         # implementing prototype design pattern
    payment_object = PaymentGatewayFactory.create_payment_gateway("Stripe")
    new_payment_object = payment_object.clone()         # implementing prototype design pattern

    pickup_location = Location(38.8951, -77.0364)
    drop_location = Location(39.8921, -78.0354)

    ride_request: RideRequest = (RideRequestBuilder().set_pickup_location(pickup_location).
                                 set_drop_location(drop_location).set_vehicle_type(vehicle_object).
                                 set_payment_method(payment_object).set_arrival_time("3").
                                 add_features("Luggage Carrier").add_features("Child Seat").build())
    print(ride_request)
    vehicle_object.ride()
    payment_object.process_payment(100)


if __name__ == '__main__':
    main()
