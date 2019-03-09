from .cards_pandas import cards_pandas
from .cards_python import cards_python
from .card_strsup_learn import cards_sup_learn

card_strs = [cards_pandas,
             cards_python,
             cards_sup_learn]

__all__ = ['card_strs']
