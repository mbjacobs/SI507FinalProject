# Define data types.
class Media:

    def __init__(self, title="No Title", author="No Author", year="No Release Year", summary="None"):
        self.title = title
        self.author = author
        self.release_yr = year
        self.summary = summary

    def __str__(self):
        return self.title + " by " + self.author + " (" + self.release_yr + ")"


class Movie (Media):

    def __init__(self, title="No Title", author="No Author", year="No Release Year",
                 summary="None", rating="No Rating", genres="None", img_url="None"):

        super().__init__(title, author, year, summary)
        self.rating = rating
        self.genres = genres
        self.img_url = img_url

    def __str__(self):
        return super().__str__() + " [" + self.rating + "]"

class Book (Media):
    def __init__(self, title="No Title", author="No Author", year="No Release Year",
                 summary="None", img_url="None"):
        super().__init__(title, author, year, summary)
        self.img_url = img_url

    def __str__(self):
        return super().__str__() + " [" + self.summary + "]"