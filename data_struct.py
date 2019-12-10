#########################################################################
# Name:  Mariah Jacobs
# Class: SI 507-003
# Date:  December 10, 2019
# File:  data_struct.py
# Purpose: Define classes.
#########################################################################
class Media:

    def __init__(self, title="No Title", author="No Author", year="No Release Year", summary="None"):
        self.title = title
        self.author = author
        self.year = year
        self.summary = summary

    def __str__(self):
        return self.title + " by " + self.author + " (" + self.year + ")"


class Movie (Media):

    def __init__(self, title="No Title", author="No Author", year="No Release Year",
                 summary="None", rating="No Rating", genres="None", img_url="None", status="No Data"):

        super().__init__(title, author, year, summary)
        self.rating = rating
        self.genres = genres
        self.img_url = img_url
        self.status = status

    def __str__(self):
        return super().__str__() + " [" + self.rating + "]"


class Book (Media):
    def __init__(self, title="No Title", author="No Author", year="No Release Year",
                 summary="None", pages=0):
        super().__init__(title, author, year, summary)
        self.pages = pages

    def __str__(self):
        return super().__str__() + " [" + str(self.pages) + "]"