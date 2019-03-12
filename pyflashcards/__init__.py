from flask import Flask

app = Flask(__name__)

from pyflashcards import routes # noqa
