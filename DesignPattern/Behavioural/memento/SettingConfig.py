class SettingState:
    def __init__(self, brightness, volume, resolution):
        self.__brightness = brightness
        self.__volume = volume
        self.__resolution = resolution

    @property
    def settings(self):
        return self.__brightness, self.__volume, self.__resolution


class Settings:
    def __init__(self):
        self.brightness = 0
        self.volume = 50
        self.resolution = "1080p"

    def configure(self, brightness, volume, resolution):
        if brightness and 0 <= brightness <= 100:
            self.brightness = brightness
        if volume and 0 <= volume <= 100:
            self.volume = volume
        if resolution:
            self.resolution = resolution

    def save(self):
        return SettingState(self.brightness, self.volume, self.resolution)

    def restore(self, settings_state: SettingState):
        self.brightness, self.volume, self.resolution = settings_state.settings

    def __str__(self):
        return f"Brightness: {self.brightness}, Volume: {self.volume}, Resolution: {self.resolution}"


class SettingsHistory:
    def __init__(self):
        self.__history = []

    def save_settings(self, memento):
        self.__history.append(memento)

    def restore_settings(self):
        self.__history.pop()
        return self.__history.pop()


def main() -> None:
    settings = Settings()
    history = SettingsHistory()

    settings.configure(70, 80, "1440p")
    history.save_settings(settings.save())
    print(settings)

    settings.configure(90, 100, "1440p")
    history.save_settings(settings.save())
    print(settings)

    settings.restore(history.restore_settings())
    print(settings)


if __name__ == '__main__':
    main()
