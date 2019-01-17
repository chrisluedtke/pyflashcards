from quiz import FlashCard

cards_effective_python = [
    FlashCard(
        ('How could this code be improved?\n\n'
         '>>> ls = [1,2,3]\n'
         '>>> for i in range(ls):\n'
         '>>>     print(i, ls[i])'),
        ('>>> for i, item in enumerate(ls):\n'
         '>>>     print(i, item)'),
        {'python', 'effective python'}
        ),
    FlashCard(
        ('How could this code be improved?\n\n'
         '>>> ls = [1,2,3]\n'
         '>>> if len(ls) != 0:\n'
         '>>>     do_something()'),
        ('Empty strings and lists implicitly evaluate to False.\n\n'
         '>>> if ls:\n'
         '>>>     do_something()'),
        {'python', 'effective python', 'item 2'}
        ),
    FlashCard(
        ("What's wrong here?\n\n"
         '>>> ls = [[0] * 3] * 3\n'
         '>>> print(ls)\n'
         '[[0, 0, 0], [0, 0, 0], [0, 0, 0]]\n'
         '>>> ls[0][1] = 2\n'
         '>>> print(ls)\n'
         '>>> [[0, 2, 0], [0, 2, 0], [0, 2, 0]]'),
        ("Lists don't contain objects - they contain references to objects.\n\n"
         '>>> ls_row = [0] * 3\n'
         '>>> ls = [ls_row.copy() for _ in range(3)]\n'
         '>>> ls[0][1] = 2\n'
         '>>> print(ls)\n'
         '[[0, 2, 0], [0, 0, 0], [0, 0, 0]]'),
        {'python', 'effective python', 'item 2'}
        ),
]
