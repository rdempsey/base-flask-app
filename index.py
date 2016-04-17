"""Main application file."""
from flask import Flask, render_template, Markup
import markdown

app = Flask(__name__)


@app.route('/')
def index():
    """The homepage of the application."""
    with open('README.md', 'r') as homepage_content:
        content = homepage_content.read()

    content = Markup(markdown.markdown(content))
    return render_template('index.html',
                           content=content)

if __name__ == "__main__":
    app.debug = True  # Comment this out when going into production
    app.run()
