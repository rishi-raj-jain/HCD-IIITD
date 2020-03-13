import webbrowser, random
from flask import Flask, render_template, request, jsonify, abort
from hcd_menu import menuJson
from course_list import courseJson
from research_list import researchJson
from research_list import facultyJson
from research_list import labsJSON
from research_list import studentsJSON
from research_list import publicationsJSON

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def index():
    return render_template('index.html', menu_value= menuJson)

@app.route("/student-policy/")
def policy():
    return render_template('policy.html', menu_value= menuJson)

@app.route("/btech-courses/")
def courses():
    return render_template('courses.html', menu_value= menuJson, courses_list= courseJson)

@app.route("/phd/")
def coursesphd():
    return render_template('phd.html', menu_value= menuJson)

@app.route("/research/")
def research():
    return render_template('research.html', menu_value= menuJson)

@app.route("/research-publications/")
def research_publications():
    return render_template('research_publications.html', menu_value= menuJson, research_list= publicationsJSON)

@app.route("/research-labs/")
def research_labs():
    return render_template('research_labs.html', menu_value= menuJson, labs_list= labsJSON)

@app.route("/contact/")
def contact():
    return render_template('contact.html', menu_value= menuJson)

@app.route("/faculty/")
def faculty():
    return render_template('faculty.html', menu_value= menuJson, faculty_list= facultyJson)

@app.route("/students/")
def students():
    return render_template('students.html', menu_value= menuJson, students_list= studentsJSON)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', menu_value= menuJson), 404

def open_browser(a):
    webbrowser.open_new('http://127.0.0.1:'+str(a))

if(__name__ == "__main__"):
    prto_num= random.randint(1000, 8000)
    open_browser(prto_num)
    app.run(host='0.0.0.0', port= prto_num)