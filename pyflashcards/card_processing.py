from pathlib import Path

from .models import DB, Deck, FlashCard, Tag

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
