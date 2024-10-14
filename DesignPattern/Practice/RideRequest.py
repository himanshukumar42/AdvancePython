from Uber import VehicleFactory, Vehicle
from Payment import PaymentGateway, PaymentGatewayFactory


class RideRequest:
    def __init__(self, vehicle_type: str = "", payment_method: str = None, pickup_time=None, features=None):
        self.vehicle_type = vehicle_type
        self.payment_method = payment_method
        self.pickup_time = pickup_time
        self.features = features or []

    def __repr__(self):
        return f"{self.__class__.__name__}({self.vehicle_type}, {self.payment_method}, {self.pickup_time}, {self.features})"


class RideRequestBuilder:
    def __init__(self):
        self.ride_request = RideRequest()

    def set_vehicle_tye(self, vehicle_type: Vehicle):
        self.ride_request.vehicle_type = vehicle_type
        return self

    def set_payment_method(self, payment_method: PaymentGateway):
        self.ride_request.payment_method = payment_method
        return self

    def set_pickup_time(self, pickup_time):
        self.ride_request.pickup_time = pickup_time
        return self

    def add_features(self, feature):
        self.ride_request.features.append(feature)
        return self

    def build(self):
        return self.ride_request


def main() -> None:
    vehicle_object = VehicleFactory.create_vehicle_ride("BookAny")
    payment_object = PaymentGatewayFactory.create_payment_gateway("Stripe")
    ride_request: RideRequest = RideRequestBuilder().set_vehicle_tye(vehicle_object).set_payment_method(payment_object).set_pickup_time("8:30 PM").add_features("Luggage Carrier").add_features("Child Seat").build()
    print(ride_request)
    vehicle_object.ride()
    payment_object.process_payment(100)


if __name__  == '__main__':
    main()
