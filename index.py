from hcd_menu import menuJson
from course_list import courseJson
from research_list import labsJSON
from research_list import facultyJson
from research_list import researchJson
from research_list import studentsJSON
from research_list import publicationsJSON
from flask import Flask, render_template, request, jsonify, abort

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.before_request
def clear_trailing():
    from flask import redirect, request
    rp = request.path
    check_url= str(rp)
    if rp != '/' and check_url.find('svg')!=-1 and check_url.find('png')!=-1 and check_url.find('jpg')!=-1: 
        return redirect(rp+'/')

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

@app.route("/sitemap.xml/")
def sitemap():
    return render_template('sitemap.xml')

@app.route("/robots.txt/")
def toboots():
    return render_template('robots.txt')

if __name__ == "__main__":
    app.run(debug= True, port= 4000)