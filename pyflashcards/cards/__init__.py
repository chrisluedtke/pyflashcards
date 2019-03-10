import os
import fnmatch

# cards_md = os.path.join('../flashcards.md')

for root,dirs,files in os.walk('.'):
    for item in fnmatch.filter(files, '*.md'):
        file_path = os.path.join(root,item)

cards_md = file_path

__all__ = ['cards_md']
