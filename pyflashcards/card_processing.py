from collections import namedtuple
from pyflashcards.cards import cards_md

FlashCard = namedtuple('FlashCard', ['question', 'answer', 'tags'])

def md_to_cards(s):
    cards = []
    q, a, t = [False, False, False]
    q_t, a_t, t_t = ['', '', '']

    for line in s.split('\n'):
        if line.startswith('---'):
            continue
        if line.lower().startswith('# QUESTION'):
            if q:
                cards.append(
                    FlashCard(question=q_t.strip(), answer=a_t.strip(),
                              tags=[x.strip() for x in t_t.split(',')])
                )
                a, t = [False, False]
                q_t, a_t, t_t = ['', '', '']
            else:
                q = True
            continue
        if line.lower().startswith('# ANSWER'):
            a = True
            continue
        if line.lower().startswith('# TAGS'):
            t = True
            continue
        if q and not a:
            q_t += '\n' + line
            continue
        if a and not t:
            a_t += '\n' + line
            continue
        if t:
            t_t += '\n' + line
            continue

    cards.append(
        FlashCard(question=q_t.strip(), answer=a_t.strip(),
                  tags=[x.strip() for x in t_t.split(',')])
    )

    return cards


def gather_cards(flashcards=cards_md):

    cards = []

    with open(flashcards) as c:

        flashcards = c.readlines()

        for flashcard in flashcards:

            cards.extend(md_to_cards(flashcard))

    return cards
