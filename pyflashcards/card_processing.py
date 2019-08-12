import random
import re
from pathlib import Path

from sqlalchemy import func

from .models import DB, Deck, FlashCard, Tag, User_Card

CARDS_DIR = Path(__file__).parent / 'cards'


def create_or_update_decks(cards_dir=CARDS_DIR):
    for filepath in cards_dir.iterdir():
        if str(filepath).endswith('.md'):
            process_md_file(filepath=filepath)

    return None


def process_md_file(filepath) -> None:
    filename = filepath.name.strip('.md')
    match = re.match(r'^\d+', filename)
    if match:
        filename = filename.strip(match.group() + ' _')
        deck_ord = int(match.group())
    else:
        deck_ord = None
    deck = get_or_create_deck(deck_name=filename, deck_ord=deck_ord)

    # create flashcards from file contents
    with open(str(filepath)) as f:
        lines = f.read().split('\n')
        lines.append('# question')  # to ensure the last question is saved

    card_order = 1
    q, a, t = [False, False, False]
    q_str, a_str, t_str = ['', '', '']

    for line in lines:
        if line.lower().strip('# ') in ('question', 'q'):
            if all([q_str, a_str]):
                create_flashcard(
                    order=card_order,
                    question=q_str.strip(),
                    answer=a_str.strip(),
                    tags=t_str,
                    deck=deck,
                )
                card_order += 1
            q, a, t = [True, False, False]
            q_str, a_str, t_str = ['', '', '']
        elif line.startswith('---'):
            continue
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


def get_or_create_deck(deck_name: str, deck_ord: int):
    instance = Deck.query.filter(Deck.name == deck_name).first()

    if instance:
        if instance.order != deck_ord:
            instance.order = deck_ord
            DB.session.commit()
    else:
        instance = Deck(name=deck_name, order=deck_ord)
        DB.session.add(instance)
        DB.session.commit()

    return instance


def create_flashcard(order: int, question: str, answer: str, tags: str,
                     deck: Deck):
    card = FlashCard.query.filter((FlashCard.question == question) |
                                  (FlashCard.answer == answer)).first()

    if card:
        card.question = question
        card.answer = answer
        card.order = order
    else:
        card = FlashCard(question=question, answer=answer, order=order)
        DB.session.add(card)

    DB.session.commit()

    if tags:
        tags = [x.strip() for x in tags.split(',')]

        for tag_name in tags:
            tag = Tag.query.filter(Tag.name == tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                DB.session.add(tag)
                DB.session.commit()

            card.tags.append(tag)  # won't duplicate tags

    deck.flashcards.append(card)  # won't duplicate cards
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
    count_query = (DB.session
                     .query(Deck.order, Deck.name, User_Card.bin_id,
                            func.count(User_Card.bin_id))
                     .join(FlashCard,
                           User_Card.flashcard_id == FlashCard.id)
                     .join(Deck,
                           FlashCard.deck_id == Deck.id)
                     .filter(User_Card.user_id == user_id)
                     .group_by(Deck.order, Deck.name, User_Card.bin_id)
                     .order_by(Deck.order)
                     .all())

    bins = ['sum', 0, 1, 2]
    count_dict = {'All': {b: 0 for b in bins}}
    for _, dk_name, bin_id, bin_count in count_query:
        if dk_name not in count_dict:
            count_dict[dk_name] = {b: 0 for b in bins}

        count_dict[dk_name][bin_id] = bin_count
        count_dict[dk_name]['sum'] += bin_count

        count_dict['All']['sum'] += bin_count
        count_dict['All'][bin_id] += bin_count

    if percentage:
        for dk_name, dk_dict in count_dict.items():
            for bin_id, bin_counts in dk_dict.items():
                percent = bin_counts / dk_dict['sum'] * 100
                count_dict[dk_name][bin_id] = f"{round(percent)}%"

    return count_dict


def order_cards_to_study(cards_to_study, user_id):
    # assign order to cards in user_cards
    random.shuffle(cards_to_study)

    for q_idx, card in enumerate(cards_to_study):
        user_card = User_Card.query.get(card.id)
        user_card.queue_idx = q_idx
        DB.session.commit()

    return True
