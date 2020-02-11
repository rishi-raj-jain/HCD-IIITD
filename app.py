import random
from flask import Flask, render_template, request, jsonify, abort
from hcd_menu import menuJson
from course_list import courseJson

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def index():
    return render_template('index.html', menu_value= menuJson)

@app.route("/courses/")
def courses():
    return render_template('courses.html', menu_value= menuJson, courses_list= courseJson)

@app.route("/contact/")
def contact():
    return render_template('contact.html', menu_value= menuJson)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', menu_value= menuJson), 404

if(__name__ == "__main__"):
    app.run(host='0.0.0.0', port= random.randint(1000, 8000))