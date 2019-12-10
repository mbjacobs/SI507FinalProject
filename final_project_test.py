#########################################################################
# Name:  Mariah Jacobs
# Class: SI 507-003
# Date:  December 10, 2019
# File:  final_project_test.py
#########################################################################
import unittest
import json
import requests
import data_struct
import sqlite3
DBNAME = 'media.db'

class Test_Database(unittest.TestCase):
    def test_bechdel_stats_table(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = 'SELECT Title FROM BechdelStats'
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertIn(('Anna Karenina',), result_list)
        self.assertIn(('Admission',), result_list)
        self.assertEqual(len(result_list), 1794)

        conn.close()

    def test_movie_table(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = '''
               SELECT Title, Year, Director
               FROM Movies
           '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertIn(('Admission', '2013','Paul Weitz',), result_list)
        self.assertEqual(len(result_list), 408)

        sql = '''
               SELECT Title
               FROM Movies WHERE Title="Up"
           '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertEqual(len(result_list), 1)

        conn.close()

    def test_books_table(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()
        sql = '''
               SELECT Title
               FROM Books
           '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertIn(('Admission',), result_list)
        self.assertEqual(len(result_list), 88)

        conn.close()

    def test_joins(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = '''
                SELECT BechdelStats.Id, BechdelStats.Status FROM BechdelStats 
                JOIN Movies ON Movies.BechdelId=BechdelStats.Id
                WHERE Movies.BechdelId=860
           '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertEqual(len(result_list), 1)
        conn.close()

class Test_Media(unittest.TestCase):
    def test_ctor(self):
        m1 = data_struct.Media()
        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m1.year, "No Release Year")
        self.assertIsInstance(m1, data_struct.Media)

    def test_str(self):
        media1 = data_struct.Media()
        self.assertEqual(media1.__str__(), "No Title by No Author (No Release Year)")

class Test_Movie(unittest.TestCase):
    def test_ctor(self):
        movie1 = data_struct.Movie()

        self.assertEqual(movie1.rating,"No Rating")
        self.assertEqual(movie1.genres, "None")
        self.assertEqual(movie1.img_url, "None")
        self.assertEqual(movie1.status,"No Data")
        self.assertIsInstance(movie1, data_struct.Movie)
        self.assertIsInstance(movie1, data_struct.Media)

    def test_str(self):
        movie = data_struct.Movie()
        self.assertEqual(movie.__str__(), "No Title by No Author (No Release Year) "
                                         "[No Rating]")
class Test_Book(unittest.TestCase):
    def test_ctor(self):
        book1 = data_struct.Book()

        self.assertEqual(book1.pages, 0)
        self.assertIsInstance(book1, data_struct.Book)
        self.assertIsInstance(book1, data_struct.Media)

    def test_str(self):
        book = data_struct.Book()
        self.assertEqual(book.__str__(), "No Title by No Author (No Release Year) "
                                          "[0]")
unittest.main()
