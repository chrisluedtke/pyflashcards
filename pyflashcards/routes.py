from pathlib import Path
import random

from flask import redirect, render_template, request, url_for
import markdown

from pyflashcards import app # noqa
from pyflashcards.card_processing import get_cards_from_md

CARDS_DIR = Path(__file__).parent / 'cards'


@app.route('/', methods=('GET', 'POST'))
def home():
    global deck_dict
    deck_dict = get_cards_from_md(CARDS_DIR)

    if request.method == 'POST':
        requested_tags = request.form.getlist('tag')

        global cards
        cards = []
        for deckname, deck in deck_dict.items():
            filt_deck = [card for card in deck
                         if set(requested_tags) & set(card.tags)]
            cards.extend(filt_deck)

        random.shuffle(cards)

        return redirect(url_for('flashcard'))

    global deck_tags
    try:
        deck_tags
    except NameError:
        deck_tags = {}
        for deckname, deck in deck_dict.items():
            tags = []
            for card in deck:
                tags.extend(card.tags)
            deck_tags[deckname] = sorted(list(set(tags)))

    return render_template('home.html', deck_tags=deck_tags)


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
