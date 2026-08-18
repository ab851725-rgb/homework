from abc import ABC, abstractmethod

class File(ABC):
    
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class TextFile(File):
    def open(self):
        print("Привет, мир!")

    def get_info(self):
        print("текстовый файл")


class ImageFile(File):
    def open(self):
        print("  /\\_/\\ ")
        print(" ( o.o )")
        print("  > ^ < ")

    def get_info(self):
        print("графический файл")


class AudioFile(File):
    def open(self):
        print("играет трек")

    def get_info(self):
        print("аудиофайл")


class VideoFile(File):
    def open(self):
        print("видео")

    def get_info(self):
        print("видеофайл")


files = [
    TextFile(),
    ImageFile(),
    AudioFile(),
    VideoFile()
]

for file in files:
    file.open()
    file.get_info()
    print("-" * 30)