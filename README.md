# pyflashcards

A simple way to log and study python tidbits.

### Database Diagram
[View on dbdiagram.io](https://dbdiagram.io/d/5d28ee1aced98361d6dc9c7c)

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
7. Run web app:
    ```
    flask run
    ```
8. Navigate to the locally served page, typically `http://localhost:5000/`

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
4. Initialize the database from your local command line
    ```
    heroku run flask shell -a pyflashcards
    from pyflashcards.card_processing import load_md_files_to_db
    DB.drop_all()
    DB.create_all()
    load_md_files_to_db()
    quit()
    ```
