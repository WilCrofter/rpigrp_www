A minimal prototype for a Flask-based website.

Requires [python3](https://www.python.org/) and [Flask](http://flask.pocoo.org/).

To run from a shell use `python3 path/to/app.py` and navigate to `http://localhost:5000` in a browser.

As a first prototype it is meant to be improved and adapted. Images were designed and can be modified with [Inkscape](https://inkscape.org.) Python, HTML, and CSS can be modified with any decent code editor.

The website's look and feel are specified by `template/layout.html` and the style sheet `static/styles.css`. The layout has an empty "content block" which is filled by individual pages. For example, the template `projects.html`file looks like this:

``` html
{% extends "layout.html" %}

{% block content %}

<h1>Our Projects</h1>
<ul>
  <li>This website</li>
  <li>Bouncing Balls</li>
  <li>Minecraft Photobooth</li>

{% endblock %}
```
It first extends `layout.html` then specifies what should be substituted in the layout's empty content block, in this case, a list of projects: Minecraft Photobooth etc.

To add a new page, first create a template like the one above and put it in the `templates` directory. Then add a few lines of python code to app.py.

``` python
@app.route('/newpage')
def newpage()
	return render_template('newpage.html')
```
Of course you would use the actual name of your page rather than "newpage." Finally add a link to your new page to the list in `layout.html`:

```html
<li><a href="newpage"/>Newpage</a></li>
```
Naturally, the pages provided are meant to illustrate how to populate a site with pages of your own design.

This initial prototype was put together for a small group of Makers who are learning web (and other) technologies via workshops and projects.
