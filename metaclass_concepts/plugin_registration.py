class PluginMeta(type):
    plugins = []

    def __new__(cls, name, bases, dct):
        cls.plugins.append(name)
        return super().__new__(cls, name, bases, dct)


class Plugin(metaclass=PluginMeta):
    pass


class VideoPlayer(Plugin):
    pass


class AudioPlayer(Plugin):
    pass


def main() -> None:
    print(PluginMeta.plugins)


if __name__ == '__main__':
    main()
