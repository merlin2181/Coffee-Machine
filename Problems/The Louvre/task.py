class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year


title_ = input()
artist_ = input()
year_ = input()

painting = Painting(title_, artist_, year_)
print(f'"{painting.title}" by {painting.artist} ({painting.year}) hangs in the {painting.museum}.')