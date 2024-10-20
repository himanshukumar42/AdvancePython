import logging


class LegacyLogger:
    def log_message(self, message: str):
        raise NotImplementedError("log_message must be implemented")


class Application:
    def __init__(self, logger: LegacyLogger):
        self.logger = logger

    def perform_task(self):
        self.logger.log_message("Task performed successfully")


class NewLogger:
    def __init__(self):
        self.logger = None

    def get_logger(self):
        if self.logger is None:
            self.logger = logging.getLogger("NewLogger")
            self.logger.setLevel(logging.DEBUG)
            output_stream = logging.StreamHandler()
            output_stream.setLevel(logging.DEBUG)
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            output_stream.setFormatter(formatter)
            self.logger.addHandler(output_stream)
        return self.logger

    def log(self, message: str):
        logger = self.get_logger()
        logger.info(message)


class LoggerAdapter(LegacyLogger):
    def __init__(self, new_logger: NewLogger):
        self.new_logger = new_logger

    def log_message(self, message: str):
        self.new_logger.log(message)


def main() -> None:
    new_logger = NewLogger()
    adapted_logger = LoggerAdapter(new_logger)

    app = Application(adapted_logger)
    app.perform_task()


if __name__ == '__main__':
    main()
