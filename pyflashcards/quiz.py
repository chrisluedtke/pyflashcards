from collections import namedtuple
from pathlib import Path
import random
from typing import List


FlashCard = namedtuple('FlashCard', ['question', 'answer', 'tags'])

CARD_DIR = Path(__file__).parent / 'cards'


def txt_to_cards(txt_path):
    cards = []
    q, a, t = [False, False, False]
    q_t, a_t, t_t = ['', '', '']

    with open(txt_path) as f:
        for line in f.readlines():
            if line.startswith('---'):
                continue
            if line.lower().startswith('question'):
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
            if line.lower().startswith('answer'):
                a = True
                continue
            if line.lower().startswith('tags'):
                t = True
                continue
            if q and not a:
                q_t += line
                continue
            if a and not t:
                a_t += line
                continue
            if t:
                t_t += line
                continue

        cards.append(
            FlashCard(question=q_t.strip(), answer=a_t.strip(),
                      tags=[x.strip() for x in t_t.split(',')])
        )

    return cards


def gather_cards():
    cards = []
    for child in CARD_DIR.iterdir():
        if str(child).endswith('.txt'):
            cards.extend(txt_to_cards(str(child)))

    return cards


def quiz():
    cards = gather_cards()

    quiz_cards = []
    while not quiz_cards:
        tag = input('Enter the tag(s) to study: ').lower()
        quiz_cards = [card for card in cards if tag in card.tags]

    input(f'Found {len(quiz_cards)} flashcards. Enter any key to begin.')
    print()

    random.shuffle(quiz_cards)
    correct = 0
    for i, card in enumerate(quiz_cards):
        i += 1
        print(f"__PROMPT-{str(i).zfill(2)}{'_' * 61}\n\n{card.question}\n\n")

        user_input = ''
        options = ['y', 'n', 'quit']
        while user_input not in options:
            user_input = input(f"Know it? {'/'.join(options)}: ").lower()

        print()

        if user_input == 'quit':
            break
        elif user_input == 'y':
            correct += 1
        elif user_input == 'n':
            pass

        print(f"__ANSWER-{str(i).zfill(2)}{'_' * 61}\n\n{card.answer}\n\n\n")
        input('')

    print(f'Quiz Complete!\nYou scored {correct} out of {len(quiz_cards)}.')
    return
