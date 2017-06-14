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

# Recall from the Flask tutorial, that `index()`
# is a python function and `@app.route` is a special Python function called a "decorator."


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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
