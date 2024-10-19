import json


class ConfigLoader:
    def __init__(self, config_file):
        self.config_file = config_file
        self._config_data = None

    def get_config(self):
        if self._config_data is None:
            with open(self.config_file, 'r') as file:
                self._config_data = json.load(file)
                print("config file is loaded.")
            return self._config_data


def main() -> None:
    config = ConfigLoader("config.json")
    db_url = config.get_config().get("DATABASE_URL")
    print(db_url)


if __name__ == "__main__":
    main()
