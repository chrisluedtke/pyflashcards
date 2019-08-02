from datetime import datetime
from os import getenv

import markdown
from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)
from sqlalchemy import func

from . import auth
from .auth import login_required
from .card_processing import (assign_cards_to_user, clear_queued_cards,
                              get_bin_card_counts, get_cards_to_study,
                              load_md_files_to_db, order_cards_to_study)
from .config import Config
from .models import DB, Deck, FlashCard, Tag, User, User_Card


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(auth.bp)
    DB.init_app(app)

    @app.shell_context_processor
    def make_shell_context():
        return {'DB': DB, 'FlashCard': FlashCard, 'Tag': Tag, 'Deck': Deck,
                'User': User, 'User_Card': User_Card}

    if getenv('FLASK_ENV') == "development":
        @app.route('/reset')
        def reset():
            DB.drop_all()
            DB.create_all()
            load_md_files_to_db()
            return redirect(url_for('index'))

    @app.route('/', methods=('GET', 'POST'))
    @login_required
    def index():
        user_id = session['user_id']

        if request.method == 'POST' and 'start_quiz' in request.form:
            error = None

            if 'bin' not in request.form or 'deck' not in request.form:
                error = 'Must select at least one category and bin.'
            else:
                cards_to_study = get_cards_to_study(
                    user_id,
                    requested_decks=request.form.getlist('deck'),
                    requested_bins=request.form.getlist('bin'),
                    requested_tags=request.form.getlist('tag')
                )
                if not cards_to_study:
                    error = 'No cards with selected categories and bins.'

            if not error:
                clear_queued_cards(user_id)
                order_cards_to_study(cards_to_study, user_id)

                return redirect(url_for('flashcard', id=cards_to_study[0].id))
            else:
                flash(error)

        assign_cards_to_user(user_id)
        bin_card_counts = get_bin_card_counts(user_id)

        return render_template('index.html', deck_counts=bin_card_counts)

    @app.route('/flashcard/<int:id>', methods=('GET', 'POST'))
    @login_required
    def flashcard(id):
        user_id = session['user_id']
        card = FlashCard.query.filter(FlashCard.id == id).one()
        user_card = User_Card.query.filter(
            User_Card.flashcard_id == id,
            User_Card.user_id == user_id
        ).one()

        queue_idx_max = DB.session.query(func.max(User_Card.queue_idx)).filter(
            User_Card.user_id == user_id
        ).scalar()

        if request.method == 'POST':
            next_idx = user_card.queue_idx + 1
            user_card.queue_idx = None

            user_card.last_attempt_date = datetime.utcnow()
            user_card.total_attempts = user_card.total_attempts + 1

            if 'pass' in request.values:
                user_card.total_successful = user_card.total_successful + 1
                if user_card.bin_id < 2:
                    user_card.bin_id = user_card.bin_id + 1
                user_card.last_attempt_successful = True
            elif 'fail' in request.values:
                if user_card.bin_id > 0:
                    user_card.bin_id = user_card.bin_id - 1
                user_card.last_attempt_successful = False

            DB.session.commit()

            next_card = User_Card.query.filter(
                User_Card.user_id == user_id,
                User_Card.queue_idx == next_idx
            ).all()

            if not next_card:
                return redirect(url_for('complete'))
            else:
                return redirect(url_for('flashcard',
                                        id=next_card[0].flashcard_id))

        question_html = markdown.markdown(
            card.question,
            extensions=['markdown.extensions.fenced_code', 'codehilite']
        )
        answer_html = markdown.markdown(
            card.answer,
            extensions=['markdown.extensions.fenced_code', 'codehilite']
        )

        deck_name = (DB.session.query(Deck.name)
                               .join(FlashCard)
                               .filter(FlashCard.id == id)
                               .one())[0]

        return render_template('flashcard.html',
                               question_html=question_html,
                               answer_html=answer_html,
                               n_total=queue_idx_max,
                               n_current=user_card.queue_idx,
                               deck_name=deck_name)

    @app.route('/complete', methods=('GET', 'POST'))
    @login_required
    def complete():
        if request.method == 'POST':
            return redirect(url_for('index'))
        return render_template('complete.html')

    return app
