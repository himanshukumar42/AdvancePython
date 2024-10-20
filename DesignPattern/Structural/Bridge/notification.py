from abc import ABC, abstractmethod


class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(NotificationChannel):
    def send(self, message):
        print(f"Sending notification via email: {message}")


class SMSNotification(NotificationChannel):
    def send(self, message):
        print(f"Sending notification via SMS: {message}")


class PushNotification(NotificationChannel):
    def send(self, message):
        print(f"Sending notification via Push: {message}")


class Alert(ABC):
    def __init__(self, notification_channel: NotificationChannel):
        self.notification_channel = notification_channel

    @abstractmethod
    def send_alert(self, message):
        pass


class SystemAlert(Alert):
    def send_alert(self, message):
        message = f"System Alert-{message}"
        self.notification_channel.send(message)


class AccountAlert(Alert):
    def send_alert(self, message):
        message = f"Account Alert-{message}"
        self.notification_channel.send(message)


class TransactionalAlert(Alert):
    def send_alert(self, message):
        message = f"Transactional Alert-{message}"
        self.notification_channel.send(message)


class Event(ABC):
    def __init__(self, notification_channel: NotificationChannel):
        self.notification_channel = notification_channel

    @abstractmethod
    def notify(self):
        pass


class UserRegistrationEvent(Event):
    def notify(self):
        message = "User successfully created."
        self.notification_channel.send(message)


class PasswordResetEvent(Event):
    def notify(self):
        message = "Password reset event"
        self.notification_channel.send(message)


class OrderConfirmationEvent(Event):
    def notify(self):
        message = "Order is confirmed."
        self.notification_channel.send(message)


class NotificationFactory:
    @staticmethod
    def create_notification_channel(channel):
        if channel == "Email":
            return EmailNotification()
        elif channel == "SMS":
            return SMSNotification()
        elif channel == "Push":
            return PushNotification()
        else:
            return None


class AlertFactory:
    @staticmethod
    def create_alert(notification_channel, alert_type):
        if alert_type == "System":
            return SystemAlert(notification_channel)
        elif alert_type == "Account":
            return AccountAlert(notification_channel)
        elif alert_type == "Transactional":
            return TransactionalAlert(notification_channel)
        else:
            return None


class EventFactory:
    @staticmethod
    def create_event(event, notification_method):
        if event == "UserRegistration":
            return UserRegistrationEvent(notification_method)
        elif event == "PasswordReset":
            return PasswordResetEvent(notification_method)
        elif event == "OrderConfirmation":
            return OrderConfirmationEvent(notification_method)


def main() -> None:
    email_object = NotificationFactory.create_notification_channel("Email")

    event_object = EventFactory.create_event("UserRegistration", email_object)
    event_object.notify()


if __name__ == '__main__':
    main()
