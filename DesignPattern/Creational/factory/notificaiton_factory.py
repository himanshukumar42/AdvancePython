from abc import ABC, abstractmethod


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


class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS Notification Sent: {message}")


class EmailNotification(Notification):
    def send(self, message):
        print(f"Email Notification Sent: {message}")


def main() -> None:
    sms = NotificationFactory.create_notification("SMS")
    email = NotificationFactory.create_notification("Email")

    sms.send("OTP is 829902")
    email.send("OTP is 829902")

    
if __name__ == '__main__':
    main()
