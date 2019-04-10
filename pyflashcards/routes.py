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

        # TODO refactor this to database
        global to_study_ids
        to_study_ids = []
        for card in FlashCard.query.all():
            for tag in card.tags:
                if tag.name in requested_tags:
                    to_study_ids.append(card.id)
                    continue
        random.shuffle(to_study_ids)

        return redirect(url_for('flashcard', id=to_study_ids[0]))

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/flashcard/<int:id>', methods=('GET', 'POST'))
def flashcard(id):
    global to_study_ids
    if request.method == 'POST':
        to_study_ids.pop(0)
        if not to_study_ids:
            return redirect(url_for('complete'))
        else:
            return redirect(url_for('flashcard', id=to_study_ids[0]))

    card = FlashCard.query.filter(FlashCard.id==id)[0]
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
