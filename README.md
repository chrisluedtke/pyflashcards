# pyflashcards

A simple way to log and study python tidbits

### Set up - Local Python
1. Clone this repository (fork it first if you want to deploy to Heroku):
```
git clone https://github.com/chrisluedtke/pyflashcards
```
2. Create flashcard markdown files in the `cards` directory. See samples for formatting.

3. Within project repository, create a virtual environment:
```
python -m venv venv
```
4. Activate the environment:
```
venv\Scripts\activate
```
5. Install requirements:
```
pip install -r requirements.txt
```
6. Run web app:
```
flask run
```
7. Navigate to the locally served page, typically `http://localhost:5000/`

### Set up - Local Docker
1. Clone this repository
2. Within project repository, build the image
```
docker build -t pyflashcards:latest .
```
3. Run the container
```
docker run -p 8000:8000 pyflashcards:latest
```

### Deploy to Heroku
1. Fork this repository to your GitHub account.
2. On Heroku, connect your GitHub account, and create an app that syncs with your forked repository.
