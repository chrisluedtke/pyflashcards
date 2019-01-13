import pandas as pd

from quiz import FlashCard

cards_pandas = [
    FlashCard(
        ('What is a key difference between pandas Series and NumPy array?'),
        ('A pandas Series can have an explicitly defined index of any type.'),
        {'pandas', 'beginner', 'week 2'}
        ),
    FlashCard(
        ('Manually code a pandas Series of integers.'),
        ('>>> data = pd.Series([1, 2, 3])\n'
         '>>> data\n'
         f'{pd.Series([1, 2, 3])}'),
        {'pandas', 'beginner', 'week 2'}
        ),
    FlashCard(
        ('Return the values of a pandas Series. What object type is it?'),
        ('>>> data = pd.Series([1, 2, 3])\n'
         '>>> data.values\n'
         f'{pd.Series([1, 2, 3]).values}\n'
         '>>> type(data.values)\n'
         "<class 'numpy.ndarray'>"),
        {'pandas', 'beginner', 'week 2'}
        ),
    FlashCard(
        ('Which standard python type is the pandas Series somewhat a \n'
         'specialization of? How so?\n'),
        ('A dictionary. A dictionary is a structure that maps arbitrary \n'
         'keys to a set of arbitrary values, and a Series is a structure \n'
         'which maps typed keys to a set of typed values. The type \n'
         'information of a Pandas Series makes it much more efficient \n'
         'than Python dictionaries for certain operations.'),
        {'pandas', 'beginner', 'week 2'}
        ),
    FlashCard(
        ('How can a pandas DataFrame be constructed?'),
        ('* a single Series object\n'
         '* a list of dicts\n'
         '* a dictionary of Series objects\n'
         '* a two-dimensional NumPy array\n'
         '* a NumPy structured array'),
        {'pandas', 'beginner', 'week 2'}
        ),
    FlashCard(
        ('How is a pandas Index object similar to a python set? How is it \n'
         'different?'),
        ('They are both immutable. However, an Index can contain duplicates. \n'
         'They both support union, intersection, etc. operations.'),
        {'pandas', 'beginner', 'week 2'}
        ),
    FlashCard(
        ('What is the benefit of using object methods instead of operators \n'
         'when applying ufuncs to Series/DataFrames?\n'
         'e.g. A + B versus A.add(B)'),
        ('The object method takes fill_value and axis arguments.'),
        {'pandas', 'beginner', 'week 2'}
        ),
]
