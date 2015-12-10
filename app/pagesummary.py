from collections import defaultdict
import requests
from bs4 import BeautifulSoup

def get_tag_summary_from_html(html):
    parser = BeautifulSoup(html, 'html.parser')
    pretty_src = parser.prettify()
    tag_counts = defaultdict(int)
    for tag in parser.findAll():
        tag_counts[tag.name] += 1
    return pretty_src, tag_counts

def get_html_summary_from_url(url):
    EMPTY = (None, None)
    if not url:
        return EMPTY
    r = requests.get(url)
    if not r or r.status_code != 200 or not r.text:
        return EMPTY
    return get_tag_summary_from_html(r.text)
