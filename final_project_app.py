#########################################################################
# Name:  Mariah Jacobs
# Class: SI 507-003
# Date:  December 10, 2019
# File:  final_project_app.py
#########################################################################
from flask import Flask, render_template, url_for, request
import final_project_model as model
import sys

app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sortby = request.form['sortby']
        sortorder = request.form['sortorder']
        media_list = model.get_media_from_db(sortby, sortorder)
    else:
        media_list = model.get_media_from_db()
    return render_template('index.html', media_list=media_list)

if __name__ == '__main__':

    if len(sys.argv) > 1 and sys.argv[1] == '--init':
        model.init_db()
        model.insert_bechdel_stats_into_db()
        model.insert_movies_into_db()
        model.insert_books_into_db()

    print('Starting Flask app...', app.name)
    app.run(debug=True)