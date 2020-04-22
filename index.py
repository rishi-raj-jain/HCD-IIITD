import re
from course_list import courseJson
from student import studentpolicyJSON
from flask import Flask, render_template, request, jsonify, abort
from research_list import labsJSON, facultyJson, researchJson, studentsJSON2017, studentsJSON2018, publicationsJSON

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.url_map.strict_slashes=False

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/student-policy/")
def policy():
    temp= render_template('policy.html', policy_list= studentpolicyJSON)
    return re.sub(' +', ' ', ''.join(temp.split('\n')))

@app.route("/btech-courses/")
def courses():
    return render_template('courses.html', courses_list= courseJson)

@app.route("/phd/")
def coursesphd():
    return render_template('phd.html')

@app.route("/research/")
def research():
    return render_template('research.html')

@app.route("/research-publications/")
def research_publications():
    return render_template('research_publications.html', research_list= publicationsJSON)

@app.route("/research-labs/")
def research_labs():
    return render_template('research_labs.html', labs_list= labsJSON)

@app.route("/contact/")
def contact():
    temp= render_template('contact.html')
    return re.sub(' +', ' ', ''.join(temp.split('\n')))

@app.route("/faculty/")
def faculty():
    temp= render_template('faculty.html', faculty_list= facultyJson, tags= request.args.get('tags'))
    return re.sub(' +', ' ', ''.join(temp.split('\n')))

@app.route("/students/")
def students():
    temp= render_template('students.html', students_list= studentsJSON2017, students_list_1= studentsJSON2018, year= request.args.get('year'))
    return re.sub(' +', ' ', ''.join(temp.split('\n')))

@app.errorhandler(404)
def page_not_found(e):
    return re.sub(' +', ' ', ''.join(render_template('404.html').split('\n'))), 404

@app.route("/sitemap.xml/")
def sitemap():
    return render_template('sitemap.xml')

@app.route("/robots.txt/")
def toboots():
    return render_template('robots.txt')

@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js'), 200, {'Content-Type': 'text/javascript'}

if __name__ == "__main__":
    app.run(debug= True, port= 4001)