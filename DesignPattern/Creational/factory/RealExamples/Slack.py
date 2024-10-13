from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message: str, recipient: str):
        pass


class EmailNotification(Notification):
    def notify(self, message: str, recipient: str):
        print(f"Sending Email Notification: {message}")


class PushNotification(Notification):
    def notify(self, message: str, recipient: str):
        print(f"Sending Push Notification: {message}")


class SMSNotification(Notification):
    def notify(self, message: str, recipient: str):
        print(f"Sending SMS Notification: {message}")


class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        if notification_type == "Email":
            return EmailNotification()
        elif notification_type == "Push":
            return PushNotification()
        elif notification_type == "SMS":
            return SMSNotification()
        else:
            ValueError(f"invalid notification type {notification_type}")


class NotificationManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(NotificationManager, cls).__new__(cls)
            cls._instance._notifications = []
        return cls._instance

    def register_notification(self, notification: Notification):
        self._notifications.append(notification)

    def notify_all(self, message: str, recipients: dict):
        for notification in self._notifications:
            notification_type = type(notification).__name__
            recipient = recipients.get(notification_type)
            if recipient:
                notification.notify(message, recipient)


def main() -> None:
    email: EmailNotification = NotificationFactory.create_notification("Email")
    push: PushNotification = NotificationFactory.create_notification("Push")
    sms: SMSNotification = NotificationFactory.create_notification("SMS")

    manager = NotificationManager()
    manager.register_notification(email)
    manager.register_notification(push)
    manager.register_notification(sms)

    message = "Hello, Welcome to our platform! "
    recipients = {
        "EmailNotification": "user@example.com",
        "SMSNotification": "+9192993923434",
        "PushNotification": "push_user_id_123",
    }
    manager.notify_all(message, recipients)


if __name__ == '__main__':
    main()
