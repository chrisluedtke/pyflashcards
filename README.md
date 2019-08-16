# pyflashcards

A simple way to log and study python tidbits.

### Database Diagram
[View on dbdiagram.io](https://dbdiagram.io/d/5d5709fbced98361d6ddaa09)

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
    pip install -r requirements_dev.txt
    ```
6. Create a `.env` with contents:
    ```
    FLASK_APP=pyflashcards:APP
    FLASK_ENV="development"
    DATABASE_URL="sqlite:///db.sqlite3"
    SECRET_KEY="you-will-never-guess"
    ```
7. Run the web app (the database will be initialized automatically):
    ```
    flask run
    ```
8. Navigate to the locally served page, typically `http://localhost:5000/`

To update cards in the app after editing the markdown decks, simply run:
```
flask shell

create_or_update_decks()
```
**Note:** If a card's question **and** answer have been updated, this will create a new card. If just the question or just the answer have changed, the original card will be updated.

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
3. Ensure you have the following environment variales on heroku:
    ```
    FLASK_APP=pyflashcards:APP
    FLASK_ENV=production
    DATABASE_URL=
    SECRET_KEY=
    ```
4. The database will initialize automatically. To reset the production database, run this from your local command line:
    ```
    heroku run flask shell -a pyflashcards
    
    DB.drop_all()
    DB.create_all()
    create_or_update_decks()
    quit()
    ```
