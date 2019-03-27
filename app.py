import os

from pyflashcards import app, db  # noqa
from pyflashcards.models import FlashCard, Tag, Deck


# objects accessible when calling `flask shell` at terminal  
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'FlashCard': FlashCard, 'Tag': Tag, 'Deck': Deck}

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
