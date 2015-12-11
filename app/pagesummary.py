from collections import defaultdict
import requests
from bs4 import BeautifulSoup

from errors import BadURL

def get_tag_summary_from_html(html):
    parser = BeautifulSoup(html, 'lxml')
    pretty_src = parser.prettify()
    tag_counts = defaultdict(int)
    for tag in parser.findAll():
        tag_counts[tag.name] += 1
    return pretty_src, tag_counts

def get_html_summary_from_url(url, timeout=15):
    EMPTY = (None, None)
    if not url:
        raise BadURL(
            message='The url is empty!',
            status_code=400)

    try:
        r = requests.get(url, timeout=timeout)
    except requests.exceptions.ConnectionError:
        raise BadURL(
            message='Unable to connect to URL!',
            status_code=400)
    except requests.exceptions.Timeout:
        raise BadURL(
            message='Timed out while connecting to the URL!',
            status_code=408)

    if not r or r.status_code != 200 or not r.text:
        raise BadURL(
            message='Unable to connect to URL!',
            status_code=400)

    # If content-type is not html, return source, but no tags
    if 'text/html' not in r.headers.get('content-type'):
        return r.text, {}

    return get_tag_summary_from_html(r.text)
