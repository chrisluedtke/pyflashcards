from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

FlashCard_Tag_assoc = DB.Table(
    'FlashCardTag',
    DB.Column('flashcard_id', DB.Integer, DB.ForeignKey('FlashCard.id')),
    DB.Column('tag_id', DB.Integer, DB.ForeignKey('Tag.id')),
)


class User(DB.Model):
    __tablename__ = 'User'
    user_id = DB.Column(DB.Integer, primary_key=True)

    username = DB.Column(DB.String(100), unique=True)
    password = DB.Column(DB.String(100), unique=True)

    def __repr__(self):
        return f'<User {self.username}>'


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
    deck_id = DB.Column(DB.Integer, DB.ForeignKey('Deck.id'))
    tags = DB.relationship('Tag', secondary=FlashCard_Tag_assoc,
                           backref='flashcards')

    def __repr__(self):
        return f'<FlashCard {self.id}>'


class Tag(DB.Model):
    __tablename__ = 'Tag'
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(100), unique=True)

    def __repr__(self):
        return f'<Tag {self.name}>'


class User_Card(DB.Model):
    __tablename__ = 'User_Card'
    id = DB.Column(DB.Integer, primary_key=True)
    user_id = DB.Column(DB.Integer, DB.ForeignKey('User.user_id'))
    flashcard_id = DB.Column(DB.Integer, DB.ForeignKey('FlashCard.id'))

    curr_box_number = DB.Column(DB.Integer, default=0)

    queue_idx = DB.Column(DB.Integer, default=None)
    total_attempts = DB.Column(DB.Integer, default=0)
    last_attempt_date = DB.Column(DB.DateTime, default=None)

    last_attempt_successful = DB.Column(DB.Boolean, default=None)
    total_successful = DB.Column(DB.Integer, default=0)

    def __repr__(self):
        return f'<User_Card {self.id}>'
