from flask import jsonify

class BadURL(Exception):
    status_code = 400
    def __init__(self, message='Unable to connect to specified URL',
                 status_code=None,
                 payload=None):
        self.message = message
        if self.status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        payload = dict(self.payload or ())
        payload['message'] = self.message
        return payload
