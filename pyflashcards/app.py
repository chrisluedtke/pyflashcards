import random

import markdown
from flask import Flask, redirect, render_template, request, url_for

from . import auth
from .card_processing import load_md_files_to_db
from .config import Config
from .models import DB, Deck, FlashCard, Tag, User


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(auth.bp)
    DB.init_app(app)

    @app.shell_context_processor
    def make_shell_context():
        return {'DB': DB, 'FlashCard': FlashCard, 'Tag': Tag, 'Deck': Deck,
                'User': User}

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        load_md_files_to_db()
        return redirect(url_for('root'))

    @app.route('/', methods=('GET', 'POST'))
    def root():
        if request.method == 'POST' and 'start_quiz' in request.form:
            requested_tags = request.form.getlist('tag')

            # TODO refactor this to database user_cards table
            global to_study_ids
            to_study_ids = []
            for card in FlashCard.query.all():
                for tag in card.tags:
                    if tag.name in requested_tags:
                        to_study_ids.append(card.id)
            random.shuffle(to_study_ids)

            return redirect(url_for('flashcard', id=to_study_ids[0]))

        deck_tags = {}
        decks = Deck.query.all()
        for deck in decks:
            tags = Tag.query.filter(
                Tag.flashcards.any(FlashCard.deck_id == deck.id)
            ).all()
            deck_tags[deck.name] = sorted([tag.name for tag in tags])

        return render_template('index.html', deck_tags=deck_tags)

    @app.route('/flashcard/<int:id>', methods=('GET', 'POST'))
    def flashcard(id):
        global to_study_ids
        if request.method == 'POST':
            to_study_ids.pop(0)
            if not to_study_ids:
                return redirect(url_for('complete'))
            else:
                return redirect(url_for('flashcard', id=to_study_ids[0]))

        card = FlashCard.query.filter(FlashCard.id == id).one()
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
            return redirect(url_for('root'))
        return render_template('complete.html')

    return app
