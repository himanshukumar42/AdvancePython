import smtplib


class EmailSender:
    def __init__(self):
        self._smtp_server = None

    def get_smtp_server(self):
        if self._smtp_server is None:
            self._smtp_server = smtplib.SMTP('smtp.gmail.com')
        return self._smtp_server

    def send_email(self, recipient, subject, body):
        smtp_server = self.get_smtp_server()
        message = f"Subject: {subject}\n\n body"
        smtp_server.sendmail("sender@example.com", recipient, message)


def main() -> None:
    email_sender = EmailSender()
    email_sender.send_email("recipient@example.com", "Test Subject", "Hello!")


if __name__ == '__main__':
    main()
