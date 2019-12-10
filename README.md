# Book && Movie

Book && Movie is a SI 507 final project designed to present users with a set of movies from FiveThirtyEight's data
set of nearly 1,800 movie titles that were scored on the Bechdel Test

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python3, Flask, knowledge of virtual environments

### Installing

In order to configure this project, please follow these steps:

1. Clone the repository onto your local system.
```
git clone https://github.com/mbjacobs/SI507FinalProject.git
```

2. Obtain (or create) the secret.py file with the necessary API keys. (For the purpose of SI 507, this was turned
in to Canvas with my submission.)

3. Place secret.py at the root level in the SI507FinalProject directory. At this point, run 'ls' on the directory.
 You should see:
```
507 Final Project Proposal V3.pdf
README.md
__pycache__
bin
data_struct.py
final_project_app.py
final_project_model.py
final_project_test.py
include
lib
media.db
media_cache.json
movies.csv
requirements.txt
secret.py
static
templates
```

4. Set up the virtual environment


## Running the tests

The "final_project_test.py" file includes unit tests to test that the data access, storage, and processing components of
the project are working correctly.

Run the following command:
```
python3 final_project_test.py
```

## Deployment

Add additional notes about how to deploy this on a live system

```
python3 final_project_test.py
```

## Built With

* [Flask](http://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/) - The templating language used with Flask
* [Python3](https://docs.python.org/3/) - The programming language on the back end
* [SQLite3](https://www.sqlite.org/docs.html) - The database backing the project

## Authors

* **Mariah Jacobs** - *Initial work* - [mbjacobs](https://github.com/mbjacobs)

## Acknowledgments

* Pedja Klasnja and Mark Newman, whose code examples helped form the basis of the Flask part of this project
* FiveThirtyEight's data set, which can be found here: https://github.com/fivethirtyeight/data/blob/master/bechdel/movies.csv
* Alison Bechdel and Liz Wallace, who are the original creators of the Bechdel test
* PurpleBooth, whose README outline I followed here: https://gist.github.com/PurpleBooth/109311bb0361f32d87a2