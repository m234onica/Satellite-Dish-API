import werkzeug.datastructures
from flask import g
from src import create_app
app = create_app("google_function")
BASE_URL = app.config.get('BASE_URL')

@app.context_processor
def url():
  return {'base_url': g.url}

@app.before_request
def before_req():
  g.url = BASE_URL

def main(request):
    with app.app_context():
        headers = werkzeug.datastructures.Headers()
        for key, value in request.headers.items():
            headers.add(key, value)
        with app.test_request_context(method=request.method, base_url=request.base_url, path=request.path, query_string=request.query_string, headers=headers, data=request.data):
            try:
                rv = app.preprocess_request()
                if rv is None:
                    rv = app.dispatch_request()
            except Exception as e:
                rv = app.handle_user_exception(e)
            response = app.make_response(rv)
            return app.process_response(response)
