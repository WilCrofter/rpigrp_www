# Recall from the Flask tutorial that to run this
# application you should:
# 1. Open a terminal in this directory
# 2. Start flask's server with the command `python3 app.py`
# 3. Open a browser to http://localhost:5000
# 4. (<ctrl>-C in the terminal stops the app.)


# Import Flask and render_template from the flask package.
from flask import Flask, render_template

# Create the app
app = Flask(__name__)

# The @app.route code below connects (routes) urls
# (web addresses) to web pages. So, for example,
# a url such as http://localhost:5000/team will
# be routed to the function team() as specified
# in the second block of code below. The team()
# function will return the web page specified
# by the template, team.html, which can be found
# in the templates directory. You need at least
# one of these routing blocks for each web page
# on the site.

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/colors')
def colors():
    return render_template('colors.html')

# This code just runs the app when the command
# python3 app.py is given. It turns on the debugger
# on, so if there's an error Flask will present
# a web page indicating what went wrong. It also
# tells the web server to respond to requests
# from anywhere (host='0.0.0.0'.)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
