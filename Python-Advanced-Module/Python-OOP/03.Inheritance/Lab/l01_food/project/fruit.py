from Various_Projects.song_album_band_project import Food
# edit inheritance source for Softuni Judge


class Fruit(Food):
    def __init__(self, name, expiration_date):
        super().__init__(expiration_date)
        self.name = name
