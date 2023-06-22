# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
#
#
# app.run()

# def app(environ, start_response):
#     """Simplest possible application object"""
#     data = b'Hello, World!\n'
#     status = '200 OK'
#     response_headers = [
#         ('Content-type', 'text/plain'),
#         ('Content-Length', str(len(data)))
#     ]
#     start_response(status, response_headers)
#     return iter([data])

# ! /usr/bin/evn python

from wsgiref.simple_server import make_server


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World"]


httpd = make_server('127.0.0.1', 8042, application)
httpd.handle_request()
