'''
    Command Line Commands so far
'''

import argparse

from .quiz import start

def get_arguments():
    description = (
        'pyflashcards is a command line tool for studying whatever topic you\'re interested in \n'
        'All done simply by calling pyflashcards -t (tag)\n'
        'If you know the answer, enter input (y) and if you do not enter (n)\n'
        'To access the next flashcard, hit [Enter]\n'
        '---\n'
        '__PROMPT-01__\n'
        '\n'
        'How can a pandas DataFrame be constructed?\n'
        '\n'
        '\n'
        'Know it? y/n/quit:\n'
        '__ANSWER-01__\n'
        '\n'
        '* a single Series object\n'
        '* a list of dicts\n'
        '* a dictionary of Series objects\n'
        '* a two-dimensional NumPy array\n'
        '* a NumPy structured array\n'
        )
    formatter = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(prog='pyflashcards', description=description, formatter_class=formatter)

    parser.add_argument('-t','--tag', metavar='TAG', default=True, nargs='+',
                        help='Tag for what topic you would like to study, for list of tags add -l or --list.')

    # parser.add_argument('-l', '--list', metavar='LIST', default=False,
    #                     help='List of tags of topics to study.')

    # parser.add_argument('')

    # I guess something to think about is if there would need to be separate arguments
    # For each tag/topic
    # i.e. machinelearning , python , pandas , keras, etc.
    # or does the -t // --tag fulfill that requirement that you're calling a tag?
    # And then the following statement could either be -l // --list
    # or the actual tag (i.e. pandas, numpy, etc.)

    return parser.parse_args()

def main():
    args = get_arguments()
    start(args)