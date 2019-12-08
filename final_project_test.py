'''
Name: Mariah Jacobs
Date: 12/8/19
Course/Discussion: SI 507-003
Assignment: Final Project Tests
'''

import unittest
import json
import requests
import data_struct

class Test_Media(unittest.TestCase):
    def test_ctor(self):
        m1 = data_struct.Media()
        m2 = data_struct.Media(None, "1999", "Prince", "1982")

        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m1.release_yr, "No Release Year")
        self.assertEqual(m2.title, "1999")
        self.assertEqual(m2.author, "Prince")
        self.assertEqual(m2.release_yr, "1982")
        self.assertIsInstance(m2, data_struct.Media)

    def test_str(self):
        media1 = data_struct.Media()
        self.assertEqual(media1.__str__(), "No Title by No Author (No Release Year)")

class Test_Movie(unittest.TestCase):
    def test_ctor(self):
        movie1 = data_struct.Movie()
        #movie2 = proj1.Movie(None, "Wonder Woman", "Patty Jenkins", "2017", 7.4, 120)

        self.assertEqual(movie1.rating,"No Rating")
        #self.assertEqual(movie2.rating, 7.4)
        #self.assertEqual(movie2.movie_length, 120)
        self.assertIsInstance(movie1, data_struct.Movie)
        self.assertIsInstance(movie1, data_struct.Media)

    def test_str(self):
        movie = data_struct.Movie()
        self.assertEqual(movie.__str__(), "No Title by No Author (No Release Year) "
                                         "[No Rating]")

class Test_Book(unittest.TestCase):
    pass

class Test_Google_Books_API(unittest.TestCase):
    pass

class Test_OMDB_API(unittest.TestCase):
    pass

class Test_Bechdel_CSV(unittest.TestCase):
    pass

class Test_Database(unittest.TestCase):
    pass

unittest.main()
