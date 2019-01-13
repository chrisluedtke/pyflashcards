from collections import namedtuple
import random
from typing import List

FlashCard = namedtuple('FlashCard', ['question', 'answer', 'tags'])

def quiz(cards: List[FlashCard]):
    tag = input('Enter a category: ').lower()
    print()

    quiz_cards = [card for card in cards if tag in card.tags]

    if not quiz_cards:
        print(f'No flashcards contain the tag "{tag}"')
        return

    random.shuffle(quiz_cards)
    correct = 0
    for i, card in enumerate(quiz_cards):
        print(f"__PROMPT{'_' * 71}\n\n{card.question}\n\n")

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

        print(f"__ANSWER{'_' * 71}\n\n{card.answer}\n\n\n")
        input('')

    print(f'Quiz Complete!\nYou scored {correct} out of {len(quiz_cards)}.')
    return
