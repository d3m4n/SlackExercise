from flask import render_template, request, session, redirect, jsonify

from forms import WebPageForm

from ..pagesummary import get_html_summary_from_url
from ..errors import BadURL
from . import main

@main.route('/', methods=['GET'])
def index():
    form = WebPageForm()
    return render_template('index.html', form=form)

@main.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@main.route('/pagesummary', methods=['GET'])
def pagesummary():
    form = WebPageForm(request.args)
    response = {}
    if form.validate():
        url = str(form.url_field.data)
        html_source, summary = get_html_summary_from_url(url)
        response['source'] = html_source
        response['summary'] = summary
    else:
        raise BadURL(message='Malformed URL!',
                     status_code=400)
    return jsonify(**response)

@main.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

@main.app_errorhandler(BadURL)
def handle_bad_url(e):
    response = jsonify(e.to_dict())
    response.status_code = e.status_code
    return response
