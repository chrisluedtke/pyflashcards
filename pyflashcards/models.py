from datetime import datetime

from pyflashcards import db


FlashCard_Tag_assoc = db.Table(
    'FlashCardTag',
    db.Column('flashcard_id', db.Integer, db.ForeignKey('FlashCard.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('Tag.id')),
)


class Deck(db.Model):
    __tablename__ = 'Deck'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    flashcards = db.relationship('FlashCard', backref='deck')

    def __repr__(self):
        return f'<Deck {self.name}>'


class FlashCard(db.Model):
    __tablename__ = 'FlashCard'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, unique=True)
    answer = db.Column(db.Text)
    tags = db.relationship('Tag', secondary=FlashCard_Tag_assoc,
                           backref='flashcards')
    deck_id = db.Column(db.Integer, db.ForeignKey('Deck.id'))
    curr_box_number = db.Column(db.Integer, default=0)
    last_attempt_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_attempt_successful = db.Column(db.Boolean, default=0)
    total_attempts = db.Column(db.Integer, default=0)
    total_successful = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<FlashCard {self.id}>'


class Tag(db.Model):
    __tablename__ = 'Tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return f'<Tag {self.name}>'
