import random

from flask import redirect, render_template, request, url_for
import markdown

from pyflashcards import app, db  # noqa
from pyflashcards.models import FlashCard, Deck, Tag
from pyflashcards.card_processing import load_md_files_to_db


@app.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST' and 'start_quiz' in request.form:
        requested_tags = request.form.getlist('tag')

        # TODO refactor this
        global cards
        cards = FlashCard.query.all()
        filtered = []
        for card in cards:
            for tag in card.tags:
                if tag.name in requested_tags:
                    filtered.append(card)
                    continue
        cards = filtered
        random.shuffle(cards)

        return redirect(url_for('flashcard'))

    if request.method == 'POST' and 'populate' in request.form:
        load_md_files_to_db()
        return redirect(url_for('home'))

    deck_tags = {}
    decks = Deck.query.all()
    for deck in decks:
        tags = Tag.query.filter(
            Tag.flashcards.any(FlashCard.deck_id == deck.id)
        ).all()
        deck_tags[deck.name] = sorted([tag.name for tag in tags])

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
