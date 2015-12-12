import os

from flask.ext.script import Manager
from gevent.wsgi import WSGIServer

from config import config
from app import create_app

CONFIGNAME = os.environ.get('APP_CONFIG', 'default')
app = create_app(CONFIGNAME)
manager = Manager(app)

if __name__ == '__main__':
    if CONFIGNAME == 'prod':
        port = os.environ.get('APP_PORT', 5000)
        wsgi_server = WSGIServer(('', port), app)
        wsgi_server.serve_forever()
    else:
        manager.run()
