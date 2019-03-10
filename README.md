# pyflashcards

A simple way to log and study python tidbits

### Set up
1. Clone this repository:
```
git clone https://github.com/chrisluedtke/pyflashcards
```
1. Create flashcard markdown files in the `cards` directory. See samples for formatting.

1. Within project repository, create a virtual environment:
```
python -m venv venv
```
1. Activate the environment (Windows method):
```
venv\Scripts\activate
```
1. Install requirements:
```
pip install -r requirements.txt
```
1. Set environment variable
```
set FLASK_APP=pyflashcards/app.py
```
1. Run web app:
```
flask run
```
1. Navigate to the locally served page, and get to studying!
