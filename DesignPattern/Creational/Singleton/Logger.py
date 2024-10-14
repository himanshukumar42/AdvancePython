class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
            cls._log_file = open("log.txt", 'a')
        return cls._instance

    def log(self, message):
        self._log_file.write(f"{message}\n")


def main() -> None:
    logger1 = Logger()
    logger2 = Logger()
    logger1.log("Log Entry 1")
    logger2.log("Log Entry 2")


if __name__ == '__main__':
    main()
