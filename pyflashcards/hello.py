from flask import Flask, request
from flask import render_template

app = Flask(__name__)

## This part will be replaced by a script that processes .md files and
## either creates a database of flashcards or just a python list of FlashCard
## objects
from collections import namedtuple

FlashCard = namedtuple('FlashCard', ['question', 'answer', 'tags'])

cards = []
cards.append(
    FlashCard(
        question='Manually code a pandas Series of integers.',
        answer="""\
ANSWER
>>> data = pd.Series([1, 2, 3])
>>> data
0    1
1    2
2    3
dtype: int64
""",
        tags=['week 2', 'beginner', 'pandas']
))

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    home page: list of flashcard tags with checkboxes,
    user checks the boxes
    """
    #   of tags they wish to study and clicks a "Start Quiz" button
    # helpful example:
    #   https://stackoverflow.com/questions/31859903/
    #   get-the-value-of-a-checkbox-in-flask
    if request.method == 'POST':
        print(request.form.getlist('tag'))
        return render_template('home.html', tags=tags)

    tags = []
    for card in cards:
        tags.extend(card.tags)
    tags = sorted(list(set(tags)))

    return render_template('home.html', tags=tags)
