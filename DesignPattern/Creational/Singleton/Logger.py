import threading


class Logger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
                cls._instance._initialize_logger()
            return cls._instance

    def _initialize_logger(self):
        self._log_file = open("app.log", "a")

    def log(self, message):
        self._log_file.write(f"{message}\n")
        self._log_file.flush()


def main() -> None:
    logger1 = Logger()
    logger2 = Logger()
    logger1.log("Log Entry 1")
    logger2.log("Log Entry 2")


if __name__ == '__main__':
    main()
