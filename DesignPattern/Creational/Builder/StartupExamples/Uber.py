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

    def set_vehicle_tye(self, vehicle_type):
        self.ride_request.vehicle_type = vehicle_type
        return self

    def set_payment_method(self, payment_method):
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
    ride_request: RideRequest = RideRequestBuilder().set_vehicle_tye("Mini").set_payment_method("Stripe").set_pickup_time("8:30 PM").add_features("Child Seat").build()

    print(ride_request)


if __name__ == '__main__':
    main()
