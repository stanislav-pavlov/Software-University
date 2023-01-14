from Various_Projects.song_album_band_project import Animal


class Lion(Animal):
    MONEY_FOR_CARE = 50

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, self.MONEY_FOR_CARE)