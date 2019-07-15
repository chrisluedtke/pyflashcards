from pathlib import Path

from .models import DB, Deck, FlashCard, Tag

CARDS_DIR = Path(__file__).parent / 'cards'


def add_to_db(question: str, answer: str, tags: str, deck: Deck):
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


def deck_str_to_db(s: str, deck: Deck) -> None:
    q, a, t = [False, False, False]
    q_str, a_str, t_str = ['', '', '']
    lines = s.split('\n')
    lines.append('---')

    for line in lines:
        q_line = line.lower().strip('# ') in ('question', 'q')
        br_line = line.startswith('---')

        if any([q_line, br_line]) and all([q_str, a_str]):
            add_to_db(
                question=q_str.strip(),
                answer=a_str.strip(),
                tags=t_str,
                deck=deck,
            )
            q, a, t = [False, False, False]
            q_str, a_str, t_str = ['', '', '']
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


def load_md_files_to_db(cards_dir=CARDS_DIR):
    for filepath in cards_dir.iterdir():
        if str(filepath).endswith('.md'):
            # create deck from filename
            filename = filepath.name.strip('.md')
            result = Deck.query.filter(Deck.name == filename).all()
            if not result:
                deck = Deck(name=filename)
                DB.session.add(deck)
                DB.session.commit()
            else:
                deck = result[0]

            with open(str(filepath)) as f:
                text = f.read()
                deck_str_to_db(s=text, deck=deck)

    return None
