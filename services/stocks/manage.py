from flask.cli import FlaskGroup

from project import app


cli = FlaskGroup(app)


if __name__ == '__main__':
    cli()

# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#    return 'Hello World'
#
# if __name__ == '__main__':
#    app.run()