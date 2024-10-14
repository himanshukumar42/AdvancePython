from abc import ABC, abstractmethod


class AudioPlayer(ABC):
    @abstractmethod
    def play(self, file):
        pass


class MP3Player(AudioPlayer):
    def play(self, file):
        if not file.endswith(".mp3"):
            raise RuntimeError(f"invalid mp3 file")
        print(f"Playing MP3 file: {file}")


class WAVPlayer(AudioPlayer):
    def play(self, file):
        if not file.endswith(".wav"):
            raise RuntimeError("invalid wav file")
        print(f"Play WAV file: {file}")


class FLACPlayer(AudioPlayer):
    def play(self, file):
        if not file.endswith(".flac"):
            raise RuntimeError("invalid flac file")
        print(f'play FLAC file: {file}')


class AudioPlayerFactory:
    @staticmethod
    def create_player(audio_type):
        if audio_type == "MP3":
            return MP3Player()
        elif audio_type == "WAV":
            return WAVPlayer()
        elif audio_type == "FLAC":
            return FLACPlayer()
        else:
            raise ValueError("unknown audio type")


def main() -> None:
    mp3: MP3Player = AudioPlayerFactory.create_player("MP3")
    mp3.play("song.mp3")


if __name__ == '__main__':
    main()
