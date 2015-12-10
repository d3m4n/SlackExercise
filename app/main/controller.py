from flask import render_template, request, session, redirect, jsonify

from forms import WebPageForm

from ..pagesummary import get_html_summary_from_url
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    form = WebPageForm()
    return render_template('index.html', form=form)

@main.route('/pagesummary', methods=['POST'])
def pagesummary():
    form = WebPageForm()
    response = {}
    if form.validate_on_submit():
        url = str(form.url_field.data)
        html_source, summary = get_html_summary_from_url(url)
        response['source'] = html_source
        response['summary'] = summary
    return jsonify(**response)

@main.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
