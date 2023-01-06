from Various_Projects.song_album_band_project import Person
from Various_Projects.song_album_band_project import Employee

class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
