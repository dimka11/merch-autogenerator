import pprint

from app import app
from app.users.views import mod
from merch_generator import generator


class LoggingMiddleware(object):
    def __init__(self, app):
        self._app = app

    def __call__(self, env, resp):
        errorlog = env['wsgi.errors']
        pprint.pprint(('REQUEST', env), stream=errorlog)

        def log_response(status, headers, *args):
            pprint.pprint(('RESPONSE', status, headers), stream=errorlog)
            return resp(status, headers, *args)

        return self._app(env, log_response)


#app.wsgi_app = LoggingMiddleware(app.wsgi_app)

app.register_blueprint(mod)
app.run(debug=True)
