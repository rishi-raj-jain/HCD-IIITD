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
    return render_template(
        'index.html', 
        event1= event1, 
        event1_details= eventsJSON.get(event1)['Image'],
        pageTitle= 'Department of Human-Centered Design, IIIT-Delhi | Human-Centered Design @ IIIT-Delhi',
        pageDescr= 'Welcome to IIIT Delhi’s Department of Human-Centered Design. With an increasing focus on user experience, the importance of Human-Computer Interaction (HCI), Interaction Design, and Design Thinking are also increasing rapidly in IT-based products and services. Digital media is at the heart of many aspects of design in areas like social media, gaming, virtual/augmented reality, etc.',
        slug= ''
    )

@app.route("/events/")
def events():
    return render_template(
        'events.html', 
        eventsJS= eventsJSON,
        pageTitle= 'Events | Human-Centered Design @ IIIT-Delhi',
        pageDescr= 'Welcome to IIIT Delhi’s Department of Human-Centered Design. With an increasing focus on user experience, the importance of Human-Computer Interaction (HCI), Interaction Design, and Design Thinking are also increasing rapidly in IT-based products and services. Digital media is at the heart of many aspects of design in areas like social media, gaming, virtual/augmented reality, etc.',
        slug= 'events'
    )

@app.route("/events/<string:number_1>")
def each_event(number_1):
    if len(number_1)>=1:
        return render_template(
            'research_projects_each.html', 
            project_head= number_1, 
            project_detail= eventsJSON.get(number_1),
            pageTitle= number_1 + ' | Human-Centered Design @ IIIT-Delhi',
            pageDescr= eventsJSON.get(number_1)['Content'],
            slug= number_1
        )
    return render_template(
        'events.html', 
        eventsJS= eventsJSON,
        pageTitle= 'Events | Human-Centered Design @ IIIT-Delhi',
        pageDescr= 'Welcome to IIIT Delhi’s Department of Human-Centered Design. With an increasing focus on user experience, the importance of Human-Computer Interaction (HCI), Interaction Design, and Design Thinking are also increasing rapidly in IT-based products and services. Digital media is at the heart of many aspects of design in areas like social media, gaming, virtual/augmented reality, etc.',
        slug= 'events'
    )

@app.route("/student-policy/")
def policy():
    return render_template(
        'policy.html', 
        policy_list= studentpolicyJSON,
        pageTitle= 'Student Conduct Policy | Human-Centered Design @ IIIT-Delhi',
        pageDescr= 'Welcome to IIIT Delhi’s Department of Human-Centered Design. With an increasing focus on user experience, the importance of Human-Computer Interaction (HCI), Interaction Design, and Design Thinking are also increasing rapidly in IT-based products and services. Digital media is at the heart of many aspects of design in areas like social media, gaming, virtual/augmented reality, etc.',
        slug= 'student-policy'
    )

@app.route("/btech-courses/")
def courses():
    return render_template(
        'courses.html', 
        courses_list= courseJson,
        pageTitle= 'B.Tech. Courses | Human-Centered Design @ IIIT-Delhi',
        pageDescr= 'Welcome to IIIT Delhi’s Department of Human-Centered Design. With an increasing focus on user experience, the importance of Human-Computer Interaction (HCI), Interaction Design, and Design Thinking are also increasing rapidly in IT-based products and services. Digital media is at the heart of many aspects of design in areas like social media, gaming, virtual/augmented reality, etc.',
        slug= 'btech-courses'
    )

@app.route("/phd/")
def coursesphd():
    return render_template(
        'phd.html',
        pageTitle= 'Ph.D. | Human-Centered Design @ IIIT-Delhi',
        pageDescr= 'Welcome to IIIT Delhi’s Department of Human-Centered Design. With an increasing focus on user experience, the importance of Human-Computer Interaction (HCI), Interaction Design, and Design Thinking are also increasing rapidly in IT-based products and services. Digital media is at the heart of many aspects of design in areas like social media, gaming, virtual/augmented reality, etc.',
        slug= 'phd'
    )

@app.route("/research-areas/")
def research():
    return render_template(
        'research.html',
        pageTitle= 'Research Areas | Human-Centered Design @ IIIT-Delhi',
        pageDescr= 'Welcome to IIIT Delhi’s Department of Human-Centered Design. With an increasing focus on user experience, the importance of Human-Computer Interaction (HCI), Interaction Design, and Design Thinking are also increasing rapidly in IT-based products and services. Digital media is at the heart of many aspects of design in areas like social media, gaming, virtual/augmented reality, etc.',
        slug= 'research-areas'
    )

@app.route("/research-publications/")
def research_publications():
    return render_template(
        'research_publications.html', 
        research_list= publicationsJSON,
        pageTitle= 'Research Publications | Human-Centered Design @ IIIT-Delhi',
        pageDescr= 'Welcome to IIIT Delhi’s Department of Human-Centered Design. With an increasing focus on user experience, the importance of Human-Computer Interaction (HCI), Interaction Design, and Design Thinking are also increasing rapidly in IT-based products and services. Digital media is at the heart of many aspects of design in areas like social media, gaming, virtual/augmented reality, etc.',
        slug= 'research-publications'
    )

@app.route("/research-labs/")
def research_labs():
    return render_template(
        'research_labs.html', 
        labs_list= labsJSON,
        pageTitle= 'Research Labs | Human-Centered Design @ IIIT-Delhi',
        pageDescr= 'Welcome to IIIT Delhi’s Department of Human-Centered Design. With an increasing focus on user experience, the importance of Human-Computer Interaction (HCI), Interaction Design, and Design Thinking are also increasing rapidly in IT-based products and services. Digital media is at the heart of many aspects of design in areas like social media, gaming, virtual/augmented reality, etc.',
        slug= 'research-labs'
    )

@app.route("/research-projects/")
def redirect_project():
    return render_template(
        'research_projects.html', 
        projects_list= projectsJSON,
        pageTitle= 'Research Projects | Human-Centered Design @ IIIT-Delhi',
        pageDescr= 'Welcome to IIIT Delhi’s Department of Human-Centered Design. With an increasing focus on user experience, the importance of Human-Computer Interaction (HCI), Interaction Design, and Design Thinking are also increasing rapidly in IT-based products and services. Digital media is at the heart of many aspects of design in areas like social media, gaming, virtual/augmented reality, etc.',
        slug= 'research-projects'
    )

@app.route("/research-projects/<string:number_1>")
def research_projects(number_1):
    if len(number_1)>=1:
        return render_template(
            'research_projects_each.html', 
            project_head= number_1, 
            project_detail= projectsJSON.get(number_1),
            pageTitle= number_1 + ' | Human-Centered Design @ IIIT-Delhi',
            pageDescr= projectsJSON.get(number_1)['Content'],
            slug= number_1
        )
    return render_template('research_projects.html', projects_list= projectsJSON)

@app.route("/contact/")
def contact():
    return render_template(
        'contact.html',
        pageTitle= 'Contact Us | Human-Centered Design @ IIIT-Delhi',
        pageDescr= 'Welcome to IIIT Delhi’s Department of Human-Centered Design. With an increasing focus on user experience, the importance of Human-Computer Interaction (HCI), Interaction Design, and Design Thinking are also increasing rapidly in IT-based products and services. Digital media is at the heart of many aspects of design in areas like social media, gaming, virtual/augmented reality, etc.',
        slug= 'contact'
    )

@app.route("/faculty/")
def faculty():
    return render_template(
        'faculty.html', 
        faculty_list= facultyJson, 
        tags= request.args.get('tags'),
        pageTitle= 'Faculty | Human-Centered Design @ IIIT-Delhi',
        pageDescr= 'Welcome to IIIT Delhi’s Department of Human-Centered Design. With an increasing focus on user experience, the importance of Human-Computer Interaction (HCI), Interaction Design, and Design Thinking are also increasing rapidly in IT-based products and services. Digital media is at the heart of many aspects of design in areas like social media, gaming, virtual/augmented reality, etc.',
        slug= 'faculty'
    )

@app.route("/thesis-defense/")
def thesis():
    return render_template(
        'thesis.html',
        pageTitle= 'Thesis Defense | Human-Centered Design @ IIIT-Delhi',
        pageDescr= 'Welcome to IIIT Delhi’s Department of Human-Centered Design. With an increasing focus on user experience, the importance of Human-Computer Interaction (HCI), Interaction Design, and Design Thinking are also increasing rapidly in IT-based products and services. Digital media is at the heart of many aspects of design in areas like social media, gaming, virtual/augmented reality, etc.',
        slug= 'thesis-defense'
    )

@app.route("/students/")
def students():
    return render_template(
        'students.html', 
        students_list= studentsJSON2017, 
        students_list_1= studentsJSON2018, 
        students_list_2= studentsJSON2019, 
        year= request.args.get('year'),
        pageDescr= 'Welcome to IIIT Delhi’s Department of Human-Centered Design. With an increasing focus on user experience, the importance of Human-Computer Interaction (HCI), Interaction Design, and Design Thinking are also increasing rapidly in IT-based products and services. Digital media is at the heart of many aspects of design in areas like social media, gaming, virtual/augmented reality, etc.',
        slug= 'students'
    )

@app.route("/phd-scholars/")
def scholars():
    return render_template(
        'scholars.html', 
        phd_scholars= phd_scholarsJSON,
        pageTitle= 'Ph.D. Scholars | Human-Centered Design @ IIIT-Delhi',
        pageDescr= 'Welcome to IIIT Delhi’s Department of Human-Centered Design. With an increasing focus on user experience, the importance of Human-Computer Interaction (HCI), Interaction Design, and Design Thinking are also increasing rapidly in IT-based products and services. Digital media is at the heart of many aspects of design in areas like social media, gaming, virtual/augmented reality, etc.',
        slug= 'phd-scholars'
    )

@app.route("/staff/")
def staff():
    return render_template(
        'staff.html', 
        faculty_list= staffJson, 
        tags= request.args.get('tags'),
        pageTitle= 'Staff | Department of Human-Centered Design, IIIT-Delhi',
        pageDescr= 'Welcome to IIIT Delhi’s Department of Human-Centered Design. With an increasing focus on user experience, the importance of Human-Computer Interaction (HCI), Interaction Design, and Design Thinking are also increasing rapidly in IT-based products and services. Digital media is at the heart of many aspects of design in areas like social media, gaming, virtual/augmented reality, etc.',
        slug= 'staff'
    )

@app.errorhandler(404)
def page_not_found(e):
    return render_template(
        '404.html', 
        pageTitle= 'Page Not Found | Department of Human-Centered Design, IIIT-Delhi',
        pageDescr= 'Welcome to IIIT Delhi’s Department of Human-Centered Design. With an increasing focus on user experience, the importance of Human-Computer Interaction (HCI), Interaction Design, and Design Thinking are also increasing rapidly in IT-based products and services. Digital media is at the heart of many aspects of design in areas like social media, gaming, virtual/augmented reality, etc.',
        slug= '404'
    ), 404

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
    app.run(debug= True, port= 4000)