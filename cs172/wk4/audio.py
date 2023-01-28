#File Name:  audio.py
#Purpose:    Demo for abstract classes
#            AudioFile class is an abstrac parent class to represent audio files
#            MP3 and WAV are derived classes, more specific audio files
#Author:     Adelaida A. Medlock
#Date:       January 29, 2021

from abc import ABC, abstractmethod    # needed to create with abstrac classes

# Parent Abstrac Class
class AudioFile(ABC):
    def __init__(self, filename):
        self.__filename = filename
    
    def getFileName(self):
        return self.__filename
    
    @abstractmethod
    def load(self):   # to be implemented by the derived classes
        pass
    
    @abstractmethod
    def play(self):   # to be implemented by the derived classes
        pass

# Derived classes    
class MP3(AudioFile):
    __extension = '.mp3'
    
    def load(self):
        print('Loading', super().getFileName() + MP3.__extension)
    
    def play(self):
        print('PLAYING', super().getFileName())
    
    
class WAV(AudioFile):
    __extension = '.wav'
    
    def load(self):
        print("Loading", super().getFileName() + WAV.__extension)
        
    def play(self):
        print('PLAYING', super().getFileName())
    

if __name__ == "__main__":
    a = MP3('rain')
    b = WAV('yesterday')
    
    myAudioFiles = [a, b]
    for file in myAudioFiles:
        file.load()
        file.play()
        print()
