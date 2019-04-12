Features to Implement
* create user_card table and track card interactions
    * user_id
    * card_id
    * curr_box_number = db.Column(db.Integer, default=0)
    * last_attempt_date = db.Column(db.DateTime, default=datetime.utcnow)
    * last_attempt_successful = db.Column(db.Boolean, default=0)
    * total_attempts = db.Column(db.Integer, default=0)
    * total_successful = db.Column(db.Integer, default=0)
    * deployed = bool
* track flashcard scores
* bucket flashcards and report schedule
* import/create flashcards
* export flashcards
