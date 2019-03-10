from collections import namedtuple


FlashCard = namedtuple('FlashCard', ['question', 'answer', 'tags'])


def str_to_cards(s: str):
    cards = []
    q, a, t = [False, False, False]
    q_t, a_t, t_t = ['', '', '']

    for line in s.split('\n'):
        if line.startswith('---'):
            continue
        if line.lower().endswith('question'):
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

    cards.append(
        FlashCard(question=q_t.strip(), answer=a_t.strip(),
                  tags=[x.strip() for x in t_t.split(',')])
    )

    return cards


def get_cards_from_md(card_dir):
    for file in card_dir.iterdir():
        if str(file).endswith('.md'):
            with open(str(file)) as f:
                cards = str_to_cards(f.read())
    return cards
