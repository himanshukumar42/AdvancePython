from abc import ABC, abstractmethod
from copy import deepcopy


class NotificationFactory:
    @staticmethod
    def create_notification(method):
        if method == "SMS":
            return SMSNotification()
        elif method == "Email":
            return EmailNotification()


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

    def clone(self):
        return deepcopy(self)


class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS Notification Sent: {message}")


class EmailNotification(Notification):
    def send(self, message):
        print(f"Email Notification Sent: {message}")


def main() -> None:
    sms = NotificationFactory.create_notification("SMS")
    email = NotificationFactory.create_notification("Email")

    my_sms_notification = SMSNotification()
    my_sms_notification.send("Hello")

    sms.send("OTP is 829902")
    email.send("OTP is 829902")

    new_email_copied_object = email.clone()
    new_email_copied_object.send("Hoolad")


if __name__ == '__main__':
    main()
