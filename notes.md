* Initial demo application with Hello World on the browser
```python
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
```

* Render HTML webpage on the browser - The HTML document must be present in
the /templates/ directory
```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Kickstart Career</title>
	</head>
	<body>
		<h1>Hello there!</h1>
		<p>You'll learn about the job openings here!</p>
	</body>
</html>
```
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def render_html():
    return render_template("home.html")
```

* Do a wireframing session to get a rough idea of how and what the webpage will
look like and the data you will require to accomplish the task

* Time - 32:30 for website template

* Any images, videos to be put on the webpage should be put inside /static/
directory

* Use Bootstrap documentation to easier change the CSS to use built-in classes
from Boostrap

* The Flask provide special syntax (called templating syntax) to enter dynamic
data into the webpage HTML, and that will be rendered on the client (browser mostly)
```python
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
```
```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
		<title>{{company}}</title>
		<!--
		<style>
			h1 {
				font-size: 40px;
				font-family: Roboto;
				font-weight: normal;
				text-align: center;
			}
			#banner {
				width: 100%;
				height: 360px;
				object-fit: cover;
			}
			h2 {
				font-size: 40px;
				font-family: Roboto;
				font-weight: normal;
				text-align: center;
			}
			p {
				font-family: Roboto;
				text-align: center;
				font-weight: normal;
			}
			#container {
				max-width: 720px;
				margin: 0 auto;
			}
		</style>
		-->
	</head>
	<body>
		<div class="container">
			<h1 class="text-center my-3">{{company}}</h1>
			<img style="height: 360px; object-fit: cover; width: 100%" src="../static/homepage-banner.jpg" class="img-fluid rounded" alt="Career Growth" height="320">
			<h2 class="my-3 text-center">About {{company}}</h2>
			<p class="my-3 text-center lead">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam mattis tempus sollicitudin. Aliquam nec nunc non ante suscipit eleifend eu id sem. Sed convallis ex vitae turpis pulvinar consectetur sit amet nec arcu. Aliquam rhoncus, nibh nec facilisis tristique, ipsum neque mattis est, vel molestie sem sem a augue. Pellentesque sodales tincidunt porta. Nullam fringilla suscipit odio. Donec ac egestas sapien. Praesent libero lacus, congue ut vulputate feugiat, condimentum sit amet odio. Sed sit amet malesuada justo, nec congue massa. Nam maximus, metus vel fringilla interdum, felis turpis blandit elit, sit amet consectetur ligula purus nec urna. Nunc efficitur, est a suscipit rhoncus, massa dolor ullamcorper leo, vel aliquam massa tortor in elit. Quisque at sem metus.</p>
			<h2 class="my-3 text-center">Open Positions</h2>
			<p class="my-3 text-center">
				{{data}}
			</p>
			<div class="my-3 text-center">
				<button class="btn btn-info">Contact Us</button>
			</div>
			<p class="my-3 text-center">Copyright: 2024 {{company}}</p>
		</div>
	</body>
</html>
```

* We can also loop through the data and add conditional statements using this
special syntax by modularising and separating the logically build part of the
webpage to a different file and then importing the file to this home.html
```html
<body>
    <div class="container">
        <h1 class="text-center my-3">{{company}}</h1>
        <img style="height: 360px; object-fit: cover; width: 100%" src="../static/homepage-banner.jpg" class="img-fluid rounded" alt="Career Growth" height="320">
        <h2 class="my-3 text-center">About {{company}}</h2>
        <p class="my-3 text-center lead">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam mattis tempus sollicitudin. Aliquam nec nunc non ante suscipit eleifend eu id sem. Sed convallis ex vitae turpis pulvinar consectetur sit amet nec arcu. Aliquam rhoncus, nibh nec facilisis tristique, ipsum neque mattis est, vel molestie sem sem a augue. Pellentesque sodales tincidunt porta. Nullam fringilla suscipit odio. Donec ac egestas sapien. Praesent libero lacus, congue ut vulputate feugiat, condimentum sit amet odio. Sed sit amet malesuada justo, nec congue massa. Nam maximus, metus vel fringilla interdum, felis turpis blandit elit, sit amet consectetur ligula purus nec urna. Nunc efficitur, est a suscipit rhoncus, massa dolor ullamcorper leo, vel aliquam massa tortor in elit. Quisque at sem metus.</p>
        <h2 class="my-3 text-center">Open Positions</h2>
        <div class="my-3">
            {% for job_listing in data %}
                {% include 'job_listing_renderer.html' %}
            {% endfor %}
        </div>
        <div class="my-3 text-center">
            <button class="btn btn-info">Contact Us</button>
        </div>
        <p class="my-3 text-center">Copyright: 2024 {{company}}</p>
    </div>
</body>
```

```html
<div class="my-3 border-bottom py-3 d-flex justify-content-md-between">
    <div mx-5>
        <h3>{{job_listing['title']}}</h3>
        <p>Location: {{job_listing['location']}}</p>
        {% if 'salary' in job_listing %}
            <p>Salary: {{job_listing['salary']}}</p>
        {% endif %}
    </div>
    <button class="btn btn-outline-primary">Apply Now</button>
</div>
```
```html
```

* We can return the data in the form of json as well using the jsonify class
```python
from flask import Flask, render_template, jsonify

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

@app.route("/api/jobs")
def job_data():
    return jsonify(jobs)
```

* 
