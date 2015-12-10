from app.pagesummary import get_tag_summary_from_html

class TestPageSummary:
    def test_basic_html(self):
        """ Tests a simple html page """
        html = '<html><head></head><body><p>Simple Html</p></body></html>'
        source, tag_summary = get_tag_summary_from_html(html)
        assert all(t in source for t in ['<html>', '</html>',
                                         '<head>', '</head>',
                                         '<body>', '</body>',
                                         '<p>', '</p>', '\n',
                                         'Simple Html'])
        assert tag_summary['html'] == 1
        assert tag_summary['body'] == 1
        assert tag_summary['p'] == 1
        assert tag_summary['head'] == 1

    def test_bad_html(self):
        """ BeautifulSoup is good at parsing bad html """
        html = '<body>'
        _, tag_summary = get_tag_summary_from_html(html)
        assert tag_summary['body'] == 1
        _, tag_summary = get_tag_summary_from_html('a')
        assert not tag_summary

    def test_no_html(self):
        _, tag_summary = get_tag_summary_from_html('')
        assert not tag_summary

    def test_html_nested_tags(self):
        html = """
        <div class="container">
            <div class="container nested">
              <span>Something</span>
            </div>
        </div>
        """
        source, tag_summary = get_tag_summary_from_html(html)
        assert tag_summary['div'] == 2
        assert tag_summary['span'] == 1
        
    def test_html_with_style_and_js(self):
        html = """
        <html>
        <head>
        <script type="text/javascript">function test(){return 'hello test!';}</script>
        <script type="text/javascript">function test2(){return 'hello again test!';}</script>
        <style type="text/css">body {background-color: #F0E68C;} </style>
        </head>
        </html>
        """
        source, tag_summary = get_tag_summary_from_html(html)
        assert tag_summary['script'] == 2
        assert tag_summary['style'] == 1
        
    
