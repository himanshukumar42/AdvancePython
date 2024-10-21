# File System
from abc import ABC, abstractmethod
import os


class FileSystem(ABC):
    @abstractmethod
    def ls(self, indent: int = 0):
        pass


class File(FileSystem):
    def __init__(self, name):
        self.name = name

    def ls(self, indent: int = 0):
        print(f"{' ' * indent}{self.name}")


class Directory(FileSystem):
    def __init__(self, name):
        self.name = name
        self.file_system_list = []

    def add(self, file: FileSystem):
        self.file_system_list.append(file)

    def create(self, path=""):
        current_path = os.path.join(path, self.name)
        if not os.path.exists(current_path):
            os.mkdir(current_path)
        for file_system in self.file_system_list:
            if isinstance(file_system, Directory):
                file_system.create(current_path)
            elif isinstance(file_system, File):
                file_path = os.path.join(current_path, file_system.name)
                with open(file_path, "w") as f:
                    f.write("")

    def search(self, search_name, path=""):
        current_path = os.path.join(path, self.name)
        if not os.path.exists(current_path):
            return None
        for file_system in self.file_system_list:
            if isinstance(file_system, File):
                if file_system.name == search_name:
                    return os.path.join(current_path, file_system.name)
            if isinstance(file_system, Directory):
                if file_system.name == search_name:
                    return os.path.join(current_path, file_system.name)
                result = file_system.search(search_name, current_path)
                if result:
                    return result
        return None

    def ls(self, indent: int = 0):
        print(f"{' ' * indent}|->{self.name}")
        for file_system in self.file_system_list:
            file_system.ls(indent+4)


def main() -> None:
    movie_directory = Directory("Movie")
    border = File("Border.mov")
    comedy_directory = Directory("Comedy Movie")
    bollywood = Directory("Bollywood")
    hul = File("hulchul.mov")
    comedy_directory.add(bollywood)
    comedy_directory.add(hul)
    movie_directory.add(border)
    movie_directory.add(comedy_directory)

    movie_directory.ls()
    # movie_directory.create()
    # print(movie_directory.search("hulchul.mov"))


if __name__ == '__main__':
    main()
