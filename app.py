"""
# import Flask class from flask module
from flask import Flask

# create an instance of the Flask class called module
app = Flask(__name__)
'''
When the Python interpreter runs a module, it sets the __name__ variable to
'__main__' if the module is being run as the main program. If the module is
being imported as a module, __name__ is set to the name of the module. In the
context of a Flask application, using __name__ allows the application to
determine its root path dynamically. This is important for Flask to locate
resources relative to the location of the module.
'''

''' create a route (the content to be returned to the client when a URL is 
requested - the route is mentioned in quotes of the @app decorator
'''
@app.route("/")
def hello_world():
    return "Hello World"
'''
The above function will be executed for the route mentioned in the
decorator immediately above it
'''
"""

"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def render_html():
    return render_template("home.html")
"""

from flask import Flask, render_template

app = Flask(__name__)

jobs = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Bengaluru, India",
        "salary": "INR 10,00,000",
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Noida, India",
        "salary": "INR 12,00,000",
    },
    {
        "id": 3,
        "title": "Frontend Engineer",
        "location": "Remote",
        "salary": "INR 15,00,000",
    },
    {
        "id": 4,
        "title": "Backend Engineer",
        "location": "San Francisco, USA",
        "salary": "$ 120,000",
    }
]

@app.route("/")
def home_page():
    return render_template("home.html", data=jobs, company="Kickstart Career")


if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)

