import re
from course_list import courseJson
from events import eventsJSON
from flask import Flask, render_template, request, jsonify, abort, redirect
from student import studentpolicyJSON, studentsJSON2017, studentsJSON2018, studentsJSON2019
from research_list import labsJSON, facultyJson, researchJson, publicationsJSON, projectsJSON, staffJson, phd_scholarsJSON

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.url_map.strict_slashes=False

@app.route("/")
def index():
    event1= next(iter(eventsJSON))
    temp= render_template('index.html', event1= event1, event1_details= eventsJSON.get(event1)['Image'])
    return re.sub(' +', ' ', ''.join(temp.split('\n')))

@app.route("/events/")
def events():
    temp= render_template('events.html', eventsJS= eventsJSON)
    return re.sub(' +', ' ', ''.join(temp.split('\n')))

@app.route("/events/<string:number_1>")
def each_event(number_1):
    if len(number_1)>=1:
        temp= render_template('research_projects_each.html', project_head= number_1, project_detail= eventsJSON.get(number_1))
        return re.sub(' +', ' ', ''.join(temp.split('\n')))
    temp= render_template('events.html', eventsJS= eventsJSON)
    return re.sub(' +', ' ', ''.join(temp.split('\n')))

@app.route("/student-policy/")
def policy():
    temp= render_template('policy.html', policy_list= studentpolicyJSON)
    return re.sub(' +', ' ', ''.join(temp.split('\n')))

@app.route("/btech-courses/")
def courses():
    temp= render_template('courses.html', courses_list= courseJson)
    return re.sub(' +', ' ', ''.join(temp.split('\n')))

@app.route("/phd/")
def coursesphd():
    return render_template('phd.html')

@app.route("/research-areas/")
def research():
    temp= render_template('research.html')
    return re.sub(' +', ' ', ''.join(temp.split('\n')))

@app.route("/research-publications/")
def research_publications():
    temp= render_template('research_publications.html', research_list= publicationsJSON)
    return re.sub(' +', ' ', ''.join(temp.split('\n')))

@app.route("/research-labs/")
def research_labs():
    temp= render_template('research_labs.html', labs_list= labsJSON)
    return re.sub(' +', ' ', ''.join(temp.split('\n')))

@app.route("/research-projects/")
def redirect_project():
    temp= render_template('research_projects.html', projects_list= projectsJSON)
    return re.sub(' +', ' ', ''.join(temp.split('\n')))

@app.route("/research-projects/<string:number_1>")
def research_projects(number_1):
    if len(number_1)>=1:
        temp= render_template('research_projects_each.html', project_head= number_1, project_detail= projectsJSON.get(number_1))
        return re.sub(' +', ' ', ''.join(temp.split('\n')))
    temp= render_template('research_projects.html', projects_list= projectsJSON)
    return re.sub(' +', ' ', ''.join(temp.split('\n')))

@app.route("/contact/")
def contact():
    temp= render_template('contact.html')
    return re.sub(' +', ' ', ''.join(temp.split('\n')))

@app.route("/faculty/")
def faculty():
    temp= render_template('faculty.html', faculty_list= facultyJson, tags= request.args.get('tags'))
    return re.sub(' +', ' ', ''.join(temp.split('\n')))

@app.route("/thesis-defense/")
def thesis():
    temp= render_template('thesis.html')
    return re.sub(' +', ' ', ''.join(temp.split('\n')))

@app.route("/students/")
def students():
    temp= render_template('students.html', students_list= studentsJSON2017, students_list_1= studentsJSON2018, students_list_2= studentsJSON2019, year= request.args.get('year'))
    return re.sub(' +', ' ', ''.join(temp.split('\n')))

@app.route("/phd-scholars/")
def scholars():
    temp= render_template('scholars.html', phd_scholars= phd_scholarsJSON)
    return re.sub(' +', ' ', ''.join(temp.split('\n')))

@app.route("/staff/")
def staff():
    temp= render_template('staff.html', faculty_list= staffJson, tags= request.args.get('tags'))
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
    app.run(debug= True, port= 4881)