import random
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def ride(self):
        pass


class Mini(Vehicle):
    def ride(self):
        print("Riding in mini car")


class Bike(Vehicle):
    def ride(self):
        print("Riding in a Bike")


class Auto(Vehicle):
    def ride(self):
        print("Riding ina Auto")


class PrimeSedan(Vehicle):
    def ride(self):
        print("Riding in a Sedan Car")


class PrimeSUV(Vehicle):
    def ride(self):
        print("Riding in a SUV Car")


class VehicleFactory:
    @staticmethod
    def create_vehicle_ride(ride_type):
        if ride_type == "Mini":
            return Mini()
        elif ride_type == "Auto":
            return Auto()
        elif ride_type == "Bike":
            return Bike()
        elif ride_type == "PrimeSedan":
            return PrimeSedan()
        elif ride_type == "PrimeSUV":
            return PrimeSUV()
        elif ride_type == "BookAny":
            vehicles = [Mini(), Auto(), Bike(), PrimeSedan(), PrimeSUV()]
            return random.choice(vehicles)
        else:
            raise ValueError(f"Invalid ride type {ride_type}")


def main() -> None:
    any_ride = VehicleFactory.create_vehicle_ride("BookAny")
    any_ride.ride()


if __name__ == '__main__':
    main()
