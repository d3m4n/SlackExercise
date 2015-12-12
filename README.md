##Summary
A web application that shows its users the source and tag summary of an html page at a location specified by a URL.

##Installation and Running
Please run the following commands from the root of the folder
* pip install virtualenv
* virtualenv venv (Optional, but recommended)
* source venv/bin/activate (Optional, but recommended)
* pip install -r requirements.txt
* python server.py runserver
  The server will now be up and running at port 5000.
* env APP_CONFIG=prod python server.py
  This will start the server on port 5000
  with prod config using Gevent for concurrency

## Running tests
To run python tests please run the following
* cd tests
* py.test
To run js tests, please open app/static/js_tests/test-pagesummary.html in
a browser

## Design
This simple web app takes as input a URL from the user and displays
the HTML source of the page to the user. A summary of all tags in the
page are displayed to the user along with their respective
counts. When a user clicks a tag, the tag is highlighted in the source
view.

The app backend is built on top of Flask, a microframework for
building Python apps.  I chose Flask because I have worked with it
very recently and found it easy to customize. Being a small framework,
it is also very easy to read Flask source code to debug it. For
parsing and processing HTML, I use BeautifulSoup with an lxml
parser. BeautifulSoup because it has a clean interface and lxml
because it is a fast C based HTML parser. I could have just as well
used something much simpler to get a list of tags and their counts,
but I also wanted to prettyprint the HTML so I went with
BeautifulSoup. Please note that I have tried to keep the physical
layout of files and folders, close to what I would have if this was a
larger application. Flask is single threaded, blocking by default.
The app should be run within a WSGI container. uwsgi and Nginx have
proven performant for handling concurrent requests, so they would be
my first choice. Other alternatives are listed at:
http://flask.pocoo.org/docs/0.10/deploying/ Note that the production
config runs the app with gevent under a WSGI container to increase
concurrency. This is no substitute for the more performant option
listed earlier.

The app's frontend is built on top of Jinja2, Bootstrap and
jQuery. Flask and Bootstrap play well together so I was able to
relatively easily come up with a bare bones template for the page. For
client side processing, I chose jQuery because the task itself was not
complicated enough to warrant the use of a more involved framework
like Angular or React. jQuery sufficed for most of my needs.  I also
made use of Underscorejs, a library which provides lots of functional
programming helpers.  My main motivation for including Underscorejs
was syntactic sugar. I liked the functional interface it
provides. Finally for client side unit testing, I made use of QUnit, a
JavaScript testing framework.
