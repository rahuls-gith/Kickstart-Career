# print("Hello World!")

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

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)
