from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

FlashCard_Tag_assoc = DB.Table(
    'FlashCardTag',
    DB.Column('flashcard_id', DB.Integer, DB.ForeignKey('FlashCard.id')),
    DB.Column('tag_id', DB.Integer, DB.ForeignKey('Tag.id')),
)


class Deck(DB.Model):
    __tablename__ = 'Deck'
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(100), unique=True)
    flashcards = DB.relationship('FlashCard', backref='deck')

    def __repr__(self):
        return f'<Deck {self.name}>'


class FlashCard(DB.Model):
    __tablename__ = 'FlashCard'
    id = DB.Column(DB.Integer, primary_key=True)
    question = DB.Column(DB.Text, unique=True)
    answer = DB.Column(DB.Text)
    tags = DB.relationship('Tag', secondary=FlashCard_Tag_assoc,
                           backref='flashcards')
    deck_id = DB.Column(DB.Integer, DB.ForeignKey('Deck.id'))
    curr_box_number = DB.Column(DB.Integer, default=0)
    last_attempt_date = DB.Column(DB.DateTime, default=datetime.utcnow)
    last_attempt_successful = DB.Column(DB.Boolean, default=0)
    total_attempts = DB.Column(DB.Integer, default=0)
    total_successful = DB.Column(DB.Integer, default=0)

    def __repr__(self):
        return f'<FlashCard {self.id}>'


class Tag(DB.Model):
    __tablename__ = 'Tag'
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(100), unique=True)

    def __repr__(self):
        return f'<Tag {self.name}>'
