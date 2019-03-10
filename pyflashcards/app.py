from pathlib import Path
import random

from flask import Flask, redirect, render_template, request, url_for
import markdown

from .card_processing import get_cards_from_md

CARDS_DIR = Path(__file__).parent / 'cards'

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def home():
    global cards
    cards = get_cards_from_md(CARDS_DIR)

    if request.method == 'POST':
        requested_tags = request.form.getlist('tag')
        cards = [card for card in cards
                 if set(requested_tags) & set(card.tags)]
        random.shuffle(cards)
        return redirect(url_for('flashcard'))

    tags = []
    for card in cards:
        tags.extend(card.tags)
    tags = sorted(list(set(tags)))

    return render_template('home.html', tags=tags)


@app.route('/flashcard', methods=('GET', 'POST'))
def flashcard():
    global cards
    if request.method == 'POST':
        cards.pop(0)
        return redirect(url_for('flashcard'))

    if not cards:
        return redirect(url_for('complete'))

    card = cards[0]
    question_html = markdown.markdown(
        card.question,
        extensions=['markdown.extensions.fenced_code']
    )
    answer_html = markdown.markdown(
        card.answer,
        extensions=['markdown.extensions.fenced_code']
    )

    return render_template('flashcard.html',
                           question_html=question_html,
                           answer_html=answer_html)


@app.route('/complete', methods=('GET', 'POST'))
def complete():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('complete.html')
