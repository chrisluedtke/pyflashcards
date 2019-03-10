# pyflashcards

A simple way to log and study python tidbits

### Set up
1. Clone this repository:
```
git clone https://github.com/chrisluedtke/pyflashcards
```
2. Create flashcard markdown files in the `cards` directory. See samples for formatting.

3. Within project repository, create a virtual environment:
```
python -m venv venv
```
4. Activate the environment (Windows method):
```
venv\Scripts\activate
```
5. Install requirements:
```
pip install -r requirements.txt
```
6. Set environment variable (Windows method):
```
set FLASK_APP=pyflashcards/app.py
```
7. Run web app:
```
flask run
```
8. Navigate to the locally served page, and get to studying!
