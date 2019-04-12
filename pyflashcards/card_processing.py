from pathlib import Path

from .models import DB, Deck, FlashCard, Tag

CARDS_DIR = Path(__file__).parent / 'cards'


def add_to_db(question, answer, tags, deck):
    result = (DB.session.query(FlashCard)
                .filter(FlashCard.question == question).all())
    if not result:
        fc = FlashCard(
            question=question,
            answer=answer,
        )
        DB.session.add(fc)
        DB.session.commit()
    else:
        fc = result[0]

    for tag in tags:
        result = DB.session.query(Tag).filter(Tag.name == tag).all()
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
    q_t, a_t, t_t = ['', '', '']

    for line in s.split('\n'):
        if line.startswith('---'):
            continue
        if line.lower().endswith('question'):
            if q:
                add_to_db(
                    question=q_t.strip(),
                    answer=a_t.strip(),
                    tags=[x.strip() for x in t_t.split(',')],
                    deck=deck,
                )
                a, t = [False, False]
                q_t, a_t, t_t = ['', '', '']
            else:
                q = True
            continue
        if line.lower().endswith('answer'):
            a = True
            continue
        if line.lower().endswith('tags'):
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

    add_to_db(
        question=q_t.strip(),
        answer=a_t.strip(),
        tags=[x.strip() for x in t_t.split(',')],
        deck=deck,
    )

    return None


def load_md_files_to_db(cards_dir: str = CARDS_DIR):
    for filepath in cards_dir.iterdir():
        if str(filepath).endswith('.md'):
            filename = filepath.name.strip('.md')
            with open(str(filepath)) as f:
                result = Deck.query.filter(Deck.name == filename).all()
                if not result:
                    deck = Deck(name=filename)
                    DB.session.add(deck)
                    DB.session.commit()
                elif len(result) > 1:
                    raise Exception('More than one deck matched the file name')
                else:
                    deck = result[0]

                text = f.read()
                deck_str_to_db(s=text, deck=deck)

    return None
