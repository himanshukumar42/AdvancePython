from abc import ABC, abstractmethod


class Booking(ABC):
    @abstractmethod
    def book(self, number):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}()"


class HotelBooking(Booking):
    def book(self, room_number):
        print(f"Booking Hotel Room: {room_number}")


class ApartmentBooking(Booking):
    def book(self, apartment_number):
        print(f"Booking Apartment: {apartment_number}")


class VillaBooking(Booking):
    def book(self, villa_number):
        print(f"Booking Villa: ", {villa_number})


class BookingFactory:
    @staticmethod
    def create_booking(booking_type):
        if booking_type == "Hotel":
            return HotelBooking()
        elif booking_type == "Apartment":
            return ApartmentBooking()
        elif booking_type == "Villa":
            return VillaBooking()
        else:
            raise ValueError("Invalid booking type")


def main() -> None:
    hotel: HotelBooking = BookingFactory.create_booking("Hotel")
    hotel.book(101)
    print(hotel)


if __name__ == '__main__':
    main()
