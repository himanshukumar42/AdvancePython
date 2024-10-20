from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def process(self, amount):
        pass


class PaypalGateway(PaymentGateway):
    def process(self, amount):
        print(f"Processing payment of ${amount} via Paypal Gateway")


class StripeGateway(PaymentGateway):
    def process(self, amount):
        print(f"Processing payment of ${amount} via Stripe Gateway")


class RazorPayGateway(PaymentGateway):
    def process(self, amount):
        print(f"Processing payment of ${amount} via RazorPay Gateway")


class PaymentGatewayFactory:
    @staticmethod
    def create_payment_gateway(payment_gateway):
        if payment_gateway == "Paypal":
            return PaypalGateway()
        elif payment_gateway == "Stripe":
            return StripeGateway()
        elif payment_gateway == "Razorpay":
            return RazorPayGateway()
        else:
            return None


class PaymentMethod(ABC):
    def __init__(self, gateway: PaymentGateway):
        self.gateway = gateway

    @abstractmethod
    def make_payment(self, amount):
        pass


class CreditCarePayment(PaymentMethod):
    def __init__(self, gateway: PaymentGateway, card_number: str, expiry_date: str, cvv: int):
        super().__init__(gateway)
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def make_payment(self, amount):
        print("Credit Card Payment - ", end=" ")
        self.gateway.process(amount)


class NetBankingPayment(PaymentMethod):
    def __init__(self, gateway: PaymentGateway, bank: str, username: str, password: str):
        super().__init__(gateway)
        self.bank = bank
        self.username = username
        self.password = password

    def make_payment(self, amount):
        print("NetBanking Payment - ", end=" ")
        self.gateway.process(amount)


class PaymentMethodFactory:
    @staticmethod
    def create_payment_method(gateway: PaymentGateway, payment_method, *args, **kwargs):
        if payment_method == "CreditCard":
            required_fields = ("card_number", "expiry_date", "cvv")
            if all(field in kwargs for field in required_fields):
                return CreditCarePayment(gateway, kwargs.get("card_number"), kwargs.get("expiry_date"), kwargs.get("cvv"))
            else:
                raise ValueError(f"required fields {required_fields}")
        elif payment_method == "NetBanking":
            required_fields = ("bank", "username", "password")
            if all(field in kwargs for field in required_fields):
                return NetBankingPayment(gateway, kwargs.get("bank"), kwargs.get("username"), kwargs.get("password"))
        else:
            return None


def main() -> None:
    paypal_object = PaymentGatewayFactory.create_payment_gateway("Paypal")
    credit_card_object = PaymentMethodFactory.create_payment_method(
        paypal_object, "CreditCard", card_number="8892920101", expiry_date="2011-01-21", cvv=577)
    credit_card_object.make_payment(1000)

    netBanking_object = PaymentMethodFactory.create_payment_method(
        paypal_object, "NetBanking", bank="SBI", username="username", password="password")
    netBanking_object.make_payment(2000)


if __name__ == '__main__':
    main()
