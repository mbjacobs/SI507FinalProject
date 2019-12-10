# Book && Movie

Book && Movie is a SI 507 final project designed to present users with a set of movies, and their corresponding book versions,
from FiveThirtyEight's data set of nearly 1,800 movie titles that were scored on the [Bechdel Test](https://en.wikipedia.org/wiki/Bechdel_test).

## Data sources

The project relied on:
* [The Google Books API](https://developers.google.com/books)
* [The Open Movie Database API](http://www.omdbapi.com/)
* [The FiveThirtyEight .csv file](https://github.com/fivethirtyeight/data/blob/master/bechdel/movies.csv)
for data-gathering.

## Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing (or grading :) ) purposes.

### Prerequisites

Python3, Flask, knowledge of virtual environments

### Installing

In order to configure this project, please follow these steps:

1. Clone the repository onto your local system.
```
$ git clone https://github.com/mbjacobs/SI507FinalProject.git
```

2. Obtain (or create) the secret.py file with the necessary API keys. (For the purpose of SI 507, this was turned
in to Canvas with my submission.)

3. Place secret.py at the root level in the SI507FinalProject directory. At this point, run 'ls' on the directory.
 You should see:
```
$ ls
507 Final Project Proposal V3.pdf
README.md
__pycache__
data_struct.py
final_project_app.py
final_project_model.py
final_project_test.py
media.db
media_cache.json
movies.csv
requirements.txt
secret.py
static
templates
```

4. Set up the virtual environment by doing the following:

* Create a new virtual environment:
```
$ virtualenv myenv
```

* Activate the virtual environment
```
$ source myenv/bin/activate
```

* Verify that there are no modules installed by pip, and then do a pip install from requirements.txt. You should see
the following list of modules:
```
(myenv) $ pip freeze
(myenv) $ pip install -r requirements.txt
(myenv) $ pip freeze

certifi==2019.11.28
chardet==3.0.4
Click==7.0
Flask==1.1.1
idna==2.8
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
requests==2.22.0
urllib3==1.25.7
Werkzeug==0.16.0
```

## Running the tests

The "final_project_test.py" file includes unit tests to test that the data access, storage, and processing components of
the project are working correctly.

Run the following command:
```
$ python3 final_project_test.py
```

## Running the application

The "final_project_app.py" file will run the application.
```
$ python3 final_project_app.py
```

If the user wants to rebuild the database backing the project, they should include the --init flag as a parameter, like so:
```
$ python3 final_project_app.py --init
```

## Data presentation

Once the Flask application is running, the user should navigate to "http://127.0.0.1:5000/index" in a web browser (or whatever
port Flask is hosting the site on, if port 5000 is already in use on your system).

IMPORTANT NOTE: the landing page of the site is index.html and the routing path is /index. Navigating to "http://127.0.0.1:5000/" will produce a 404 not found error. Without specifying /index in the route, the sorting of the table would not work correctly. This is "feature" I will investigate in the future.

The user should see a web page with a table of books and movie information presented to them. There is the option to
sort the table by different column types (Type, Title, Author, or Bechdel Status) in either ascending or descending order.
The user must select an option for EACH radio button, and then click the Update button in order to change the presentation of results in the table.

## Application Structure
This application follows the MVC (Model-View-Controller) design pattern. The View layer is index.html, which is found in
/templates and handles the presentation of the web page. The Controller layer is final_project_app.py, which calls functions from
the model and runs the Flask application based on the data it receives. The Model layer is final_project_model.py, which
contains all of the logic that reads data from the various data sources, builds and queries, the database, and populates
the Movie and Book data structures (stored in data_struct.py) used in this project.

The most significant data-processing function is get_media_from_db(), which queries the database for movies and books,
and creates a list of objects for each data set based on the returned query result. The two lists are then merged and passed off
to the application layer in order to populate the table in the data presentation layer.

## Built With

* [Flask](http://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/) - The templating language used with Flask
* [Python3](https://docs.python.org/3/) - The programming language on the back end
* [SQLite3](https://www.sqlite.org/docs.html) - The database backing the project

## Authors

* **Mariah Jacobs** - *Initial work* - [mbjacobs](https://github.com/mbjacobs)

## Acknowledgments

* Pedja Klasnja and Mark Newman, whose code examples helped form the basis of the Flask part of this project, and whose
instructions for running a project using someone else's virtual environment are replicated here
* FiveThirtyEight's data set, which can be found here: https://github.com/fivethirtyeight/data/blob/master/bechdel/movies.csv
* Alison Bechdel and Liz Wallace, who are the original creators of the Bechdel test
* PurpleBooth, whose README outline I followed here: https://gist.github.com/PurpleBooth/109311bb0361f32d87a2
