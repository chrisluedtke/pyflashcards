import random
from pathlib import Path

from sqlalchemy import func

from .models import DB, Deck, FlashCard, Tag, User_Card

CARDS_DIR = Path(__file__).parent / 'cards'


def load_md_files_to_db(cards_dir=CARDS_DIR):
    for filepath in cards_dir.iterdir():
        if str(filepath).endswith('.md'):
            process_md_file(filepath=filepath)

    return None


def process_md_file(filepath) -> None:
    deck = create_deck(deck_name=filepath.name.strip('.md'))

    # create flashcards from file contents
    with open(str(filepath)) as f:
        lines = f.read().split('\n')
        lines.append('---')

    q, a, t = [False, False, False]
    q_str, a_str, t_str = ['', '', '']

    for line in lines:
        q_line = line.lower().strip('# ') in ('question', 'q')
        br_line = line.startswith('---')

        if any([q_line, br_line]) and all([q_str, a_str]):
            create_flashcard(
                question=q_str.strip(),
                answer=a_str.strip(),
                tags=t_str,
                deck=deck,
            )
            q, a, t = [False, False, False]
            q_str, a_str, t_str = ['', '', '']
        elif br_line:
            continue
        elif q_line:
            q = True
        elif line.lower().strip('# ') in ('answer', 'a'):
            a = True
        elif line.lower().strip('# ') in ('tag', 'tags', 't'):
            t = True
        elif q and not a:
            q_str += '\n' + line
        elif a and not t:
            a_str += '\n' + line
        elif t:
            t_str += '\n' + line

    return None


def create_deck(deck_name: str):
    result = Deck.query.filter(Deck.name == deck_name).all()
    if not result:
        deck = Deck(name=deck_name)
        DB.session.add(deck)
        DB.session.commit()
    else:
        deck = result[0]

    return deck


def create_flashcard(question: str, answer: str, tags: str, deck: Deck):
    result = FlashCard.query.filter(
        FlashCard.question == question
    ).all()
    if not result:
        fc = FlashCard(question=question, answer=answer)
        DB.session.add(fc)
        DB.session.commit()
    else:
        fc = result[0]

    if tags:
        tags = [x.strip() for x in tags.split(',')]

        for tag in tags:
            result = Tag.query.filter(Tag.name == tag).all()
            if not result:
                t = Tag(name=tag)
                DB.session.add(t)
                DB.session.commit()
            else:
                t = result[0]

            fc.tags.append(t)

    deck.flashcards.append(fc)
    DB.session.commit()

    return None


def clear_queued_cards(user_id):
    cards_to_clear = User_Card.query.filter(
        User_Card.user_id == user_id,
        User_Card.queue_idx.isnot(None),
    ).all()

    for card in cards_to_clear:
        card.queue_idx = None

    DB.session.commit()

    return True


def get_cards_to_study(user_id, requested_decks, requested_bins,
                       requested_tags):
    requested_bins = [int(i) for i in requested_bins]

    if 'All' in requested_decks:
        deck_names = DB.session.query(Deck.name).all()
        requested_decks = [i for i, in deck_names]

    cards_to_study = (User_Card.query
                               .filter(User_Card.user_id == user_id,
                                       User_Card.bin_id.in_(requested_bins))
                               .join(FlashCard,
                                     User_Card.flashcard_id == FlashCard.id)
                               .join(Deck,
                                     FlashCard.deck_id == Deck.id)
                               .filter(
                                   FlashCard.tags.any(
                                       Tag.name.in_(requested_tags)
                                   ) | Deck.name.in_(requested_decks))
                               .all())

    return cards_to_study


def assign_cards_to_user(user_id):
    """Create a User_Card record for all existing cards"""
    # TODO: this can probably be queried better
    user_card_ids = (DB.session.query(User_Card.flashcard_id)
                               .filter(User_Card.user_id == user_id).all())
    unassigned_cards = FlashCard.query.filter(
        ~FlashCard.id.in_([i for i, in user_card_ids])
    ).all()

    for card in unassigned_cards:
        user_card = User_Card(user_id=user_id, flashcard_id=card.id)
        DB.session.add(user_card)
        DB.session.commit()

    return True


def get_bin_card_counts(user_id, percentage=False):
    """Count the number of cards in each bin in each deck"""
    deck_counts = (DB.session
                     .query(Deck.name, User_Card.bin_id,
                            func.count(User_Card.bin_id))
                     .join(FlashCard,
                           User_Card.flashcard_id == FlashCard.id)
                     .join(Deck,
                           FlashCard.deck_id == Deck.id)
                     .filter(User_Card.user_id == user_id)
                     .group_by(Deck.name, User_Card.bin_id).all())

    d = {'All': {'sum': 0, 0: 0, 1: 0, 2: 0}}
    for deck_name, bin_id, count in deck_counts:
        if deck_name not in d:
            d[deck_name] = {}
            d[deck_name]['sum'] = 0
        d[deck_name][bin_id] = count
        d[deck_name]['sum'] += count

        d['All']['sum'] += count
        d['All'][bin_id] += count

    for deck_name, _ in d.items():
        for bin_id in ['sum', 0, 1, 2]:
            if bin_id not in d[deck_name]:
                d[deck_name][bin_id] = 0
            if percentage:
                percent = (d[deck_name][bin_id] / d[deck_name]['sum']) * 100
                d[deck_name][bin_id] = f"{round(percent)}%"

    return d


def order_cards_to_study(cards_to_study, user_id):
    # assign order to cards in user_cards
    random.shuffle(cards_to_study)

    for q_idx, card in enumerate(cards_to_study):
        user_card = User_Card.query.get(card.id)
        user_card.queue_idx = q_idx
        DB.session.commit()

    return True
