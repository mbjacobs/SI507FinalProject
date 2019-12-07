#########################################################################
# Name:  Mariah Jacobs
# Class: SI 507-003
# Date:  December 11, 2019
# File:  final_project.py
#########################################################################
import sqlite3
import csv
import json
import sys
import requests
import data_structures
import api_data

#Define constants and initialize cache file.
DBNAME = 'media.db'
BECHDELCSV = 'movies.csv'
CACHE_FNAME = 'media_cache.json'

try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

#########################################################################
# Initialize media.db file by creating tables for Books, Movies, and
# BechdelStats.
#  params: None
# returns: None
#########################################################################
def init_db():
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    # Drop tables
    statement = '''
        DROP TABLE IF EXISTS 'Books';
    '''
    cur.execute(statement)

    statement = '''
        DROP TABLE IF EXISTS 'Movies';
    '''
    cur.execute(statement)

    statement = '''
        DROP TABLE IF EXISTS 'BechdelStats';
    '''
    cur.execute(statement)

    conn.commit()

    # Create tables
    statement = '''
        CREATE TABLE Books (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL, 
            Year TEXT NOT NULL,
            Author TEXT NOT NULL,
            Description BLOB,
            MovieId INTEGER,
            FOREIGN KEY(MovieId) REFERENCES Movie(Id)
        );
    '''
    cur.execute(statement)

    statement = '''
            CREATE TABLE Movies (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Title TEXT NOT NULL, 
                Year TEXT NOT NULL,
                Director TEXT NOT NULL,
                Rating TEXT,
                Genre TEXT,
                Plot BLOB,
                PosterURL TEXT,
                BechdelId INTEGER NOT NULL,
                FOREIGN KEY(BechdelId) REFERENCES BechdelStats(Id)
            );
        '''
    cur.execute(statement)

    statement = '''
        CREATE TABLE BechdelStats (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL,
            Year INT NOT NULL, 
            Status TEXT NOT NULL,
            Budget REAL NOT NULL,
            GrossIncome REAL NOT NULL
        );
    '''
    cur.execute(statement)

    conn.commit()
    conn.close()

#########################################################################
# Read CSV file with > 1000 lines and insert values into media.db.
#  params: None
# returns: None
#########################################################################
def insert_bechdel_stats_into_db():
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    # Insert data to Bechdel Stats table
    with open(BECHDELCSV, encoding='utf-8') as csv_data_file:
        csv_reader = csv.reader(csv_data_file)
        next(csv_reader)

        for bechdel_movie in csv_reader:
            year = bechdel_movie[0]
            title = bechdel_movie[2]
            status = bechdel_movie[5]
            budget = bechdel_movie[6]
            gross = bechdel_movie[7]

            insertion = (None, title, year, status, budget, gross)
            statement = 'INSERT INTO "BechdelStats" '
            statement += 'VALUES (?, ?, ?, ?, ?, ?)'

            cur.execute(statement, insertion)
            conn.commit()

    conn.close()

#########################################################################
# Make requests to cache or Open Movie Database API for movies on the
# Bechdel list and insert retreived data into media.db.
#  params: None
# returns: None
#########################################################################
def insert_movies_into_db():
    titles_list = []
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    titles_list = get_bechdel_titles(cur, titles_list)

    for title in titles_list:
        movie_resp = make_request_using_cache(title[0], "movie")

        if movie_resp["Response"] == "True" and title[0] == movie_resp["Title"]:

            #Look up foreign key for BechdelId in BechdelStats table
            statement = "SELECT Id FROM BechdelStats WHERE Title=?"
            result = cur.execute(statement, (movie_resp["Title"],))
            for row in result:
                bechdel_id = int(row[0])

            insertion = (None, movie_resp["Title"], movie_resp["Year"], movie_resp["Director"], movie_resp["Rated"],
                   movie_resp["Genre"], movie_resp["Plot"], movie_resp["Poster"], bechdel_id)
            statement = 'INSERT INTO "Movies" '
            statement += "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cur.execute(statement, insertion)
            conn.commit()

    conn.close()

#########################################################################
# Make requests to cache or Google Books API for books on the
# Bechdel list and insert retreived data into media.db.
#  params: None
# returns: None
#########################################################################
def insert_books_into_db():
    titles_list = []
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    book_is_found = False

    #titles_list = get_bechdel_titles(cur, titles_list)
    statement = "SELECT Movies.Title FROM Movies"
    results = cur.execute(statement)
    movie_titles_tuple = results.fetchall()

    #Process title data by converting immutable tuple to mutable list
    for title in movie_titles_tuple:
        titles_list.append(list(title))

    for title in titles_list:
        title[0]=title[0].replace(" ", "-")


    for title in titles_list:
        book_resp = make_request_using_cache(title[0], "book")

        #Select an edition of the book based on returned results
        print(book_resp)


        if "items" in book_resp.keys(): #Ensures book_resp has returned books, not an error resp

            #Loop through all of the books returned to find the one the referenced in movie list
            for book in book_resp["items"]:
                book_title = book["volumeInfo"]["title"].replace(" ", "-")

                if  title[0] == book_title and "subtitle" not in book["volumeInfo"] and \
                        book_is_found == False:
                    try:
                        book_year = book["volumeInfo"]["publishedDate"]
                    except:
                        book_year = "Unknown"
                    try:
                        book_author = book["volumeInfo"]["authors"][0]
                    except:
                        book_author = "Unknown"
                    try:
                        book_description = book["volumeInfo"]["description"]
                    except:
                        book_description = "None"

                    #print(book_title, book_year, book_author, book_description)
                    book_is_found = True

                    # Look up foreign key for movie_id from Movies table
                    statement = "SELECT Id FROM Movies WHERE Title=?"
                    result = cur.execute(statement, (book_title,))
                    for row in result:
                        movie_id = int(row[0])
                        #print(movie_id)

                    insertion = (None, book_title, book_year, book_author, book_description, movie_id)
                    statement = 'INSERT INTO "Books" '
                    statement += "VALUES (?, ?, ?, ?, ?, ?)"
                    cur.execute(statement, insertion)
                    conn.commit()

            book_is_found = False
    conn.close()


#########################################################################
#
#  params:         cur -
#          titles_list -
# returns:
#########################################################################
def get_bechdel_titles(cur, titles_list):
    #Query Bechdel Stats table to get the list of titles in set of movies
    statement = "SELECT BechdelStats.Title FROM BechdelStats"
    results = cur.execute(statement)
    titles_tuple = results.fetchall()

    #Process title data by converting immutable tuple to mutable list
    for title in titles_tuple:
        titles_list.append(list(title))

    for title in titles_list:
        title[0]=title[0].replace(" ", "-")

    return titles_list


#########################################################################
#  Make request or retrieve previous request from cache
#  params:      title - title of the media
#          media_type - string to distinguish book from movie title
# returns: cached data associated with dict entry at that url
#########################################################################
def make_request_using_cache(title, media_type):
    if media_type == "movie":
        url = "http://www.omdbapi.com/?apikey=" + api_data.OMDB_ACCESS_KEY + "&t=" + title
    elif media_type == "book":
        url = "https://www.googleapis.com/books/v1/volumes?q=" + title
    unique_ident = url

    ## First, look in the cache to see if we already have this data
    if unique_ident in CACHE_DICTION:
        print("Getting cached data from " + unique_ident + "...")
        return CACHE_DICTION[unique_ident]

    ## If not, fetch the data afresh, add it to the cache,
    ## then write the cache to file.
    print("Making a request for new data from " + url + "...")

    # Make the request and cache the new data
    resp = requests.get(url)
    CACHE_DICTION[unique_ident] = json.loads(resp.text)
    dumped_json_cache = json.dumps(CACHE_DICTION)
    fw = open(CACHE_FNAME,"w")
    fw.write(dumped_json_cache)
    fw.close() # Close the open file
    return CACHE_DICTION[unique_ident]

if __name__=="__main__":

    # if len(sys.argv) > 1 and sys.argv[1] == '--init':
    init_db()
    insert_bechdel_stats_into_db()
    insert_movies_into_db()
    insert_books_into_db()
