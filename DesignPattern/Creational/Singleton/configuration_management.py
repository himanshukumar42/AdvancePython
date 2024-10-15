import threading


class Config:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Config, cls).__new__(cls, *args, **kwargs)
                cls._instance._initialize_config()
            return cls._instance

    def _initialize_config(self):
        self.settings = {
            "DB_HOST": "localhost",
            "DB_USER": "root",
            "DB_PASSWORD": "password"
        }

    def get(self, key):
        return self.settings.get(key)

    def __getitem__(self, item):
        return self.settings.get(item)

    def __setitem__(self, key, value):
        self.settings[key] = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.settings})"


def main() -> None:
    config1 = Config()
    config2 = Config()
    print(config1)
    print(config2)
    print(config1 is config2)
    print(config1.get("DB_HOST"))
    print(config1["DB_HOST"])
    config1["DB_HOST"] = "postgres"
    print(config1)
    print(config2)


if __name__ == '__main__':
    main()
