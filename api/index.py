"""Main application file."""
from flask import Flask, render_template, Markup
from flask_restful import Resource, Api, reqparse
import markdown
import sqlite3

app = Flask(__name__)
api = Api(app)

"""Api"""


class CreateUser(Resource):
    """Create a user."""

    def post(self):
        """Return a success message."""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('email',
                                type=str,
                                help='Email address to create user')
            parser.add_argument('password',
                                type=str,
                                help='Password to create user')
            args = parser.parse_args()

            user_email = args['email']
            user_password = args['password']

            return {
                'Email': user_email,
                'Password': user_password
            }
        except Exception as e:
            return {'error': str(e)}

api.add_resource(CreateUser, '/create-user')

"""Static Pages"""


@app.route('/')
def index():
    """The homepage of the application."""
    with open('../README.md', 'r') as homepage_content:
        content = homepage_content.read()

    content = Markup(markdown.markdown(content))
    return render_template('index.html',
                           content=content)

if __name__ == "__main__":
    app.debug = True  # Comment this out when going into production
    app.run()
