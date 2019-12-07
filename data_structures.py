# Define data types.
class Media:

    def __init__(self, title="No Title", author="No Author", year="No Release Year"):
        self.title = title
        self.author = author
        self.release_yr = year

    def __str__(self):
        return self.title + " by " + self.author + " (" + self.release_yr + ")"


class Movie (Media):

    def __init__(self, title="No Title", author="No Author", year="No Release Year",
                 rating="No Rating", movie_length=0):

        super().__init__(title, author, year)
        self.rating = rating
        self.movie_length = movie_length

    def __str__(self):
        return super().__str__() + " [" + self.rating + "]"

class Book (Media):
    pass