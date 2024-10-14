from abc import ABC, abstractmethod


class SMSNotification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class EmailNotification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class BasicSMSNotification(SMSNotification):
    def notify(self, message):
        print(f"Basic SMS Notification: {message}")


class PremiumSMSNotification(SMSNotification):
    def notify(self, message):
        print(f"Premium SMS Notification: {message}")


class BasicEmailNotification(EmailNotification):
    def notify(self, message):
        print(f"Basic Email Notification: {message}")


class PremiumEmailNotification(EmailNotification):
    def notify(self, message):
        print(f"Premium Email Notification: {message}")


class NotificationFactory(ABC):
    @abstractmethod
    def create_sms_notification(self) -> SMSNotification:
        pass

    @abstractmethod
    def create_email_notification(self) -> EmailNotification:
        pass


class BasicNotificationFactory(NotificationFactory):
    def create_sms_notification(self) -> SMSNotification:
        return BasicSMSNotification()

    def create_email_notification(self) -> EmailNotification:
        return BasicEmailNotification()


class PremiumNotificationFactory(NotificationFactory):
    def create_sms_notification(self) -> SMSNotification:
        return PremiumSMSNotification()

    def create_email_notification(self) -> EmailNotification:
        return PremiumEmailNotification()


def create_notification(factory: NotificationFactory):
    sms = factory.create_sms_notification()
    email = factory.create_email_notification()

    sms.notify("OTP is 829222")
    email.notify("OTP is 829222")


def main() -> None:
    basic_factory = BasicNotificationFactory()
    create_notification(basic_factory)

    premium_factory = PremiumNotificationFactory()
    create_notification(premium_factory)


if __name__ == '__main__':
    main()
