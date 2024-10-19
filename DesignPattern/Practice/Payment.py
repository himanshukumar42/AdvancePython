from abc import ABC, abstractmethod
from copy import deepcopy


class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    def clone(self):
        return deepcopy(self)

    def __repr__(self):
        return f"{self.__class__.__name__}()"


class PaypalPaymentGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processed payment of ${amount} via Paypal")

    def paypal_method(self):
        print(f"{self.__class__.__name__} related method")


class StripePaymentGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processed payment of ${amount} via Stripe")

    def hello_method(self):
        print(f"Doing hello to {self.__class__.__name__}")


class PaymentGatewayFactory:
    @staticmethod
    def create_payment_gateway(gateway):
        if gateway == "Stripe":
            return StripePaymentGateway()
        elif gateway == "Paypal":
            return PaypalPaymentGateway()
        else:
            raise ValueError("Unknown Payment Gateway")
