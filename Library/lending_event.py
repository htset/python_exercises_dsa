from datetime import datetime

class LendingEvent:
    def __init__(self, book_title: str, user_name: 
                 str, lending_date: datetime, returned: int):
        self.book_title = book_title
        self.user_name = user_name
        self.lending_date = lending_date
        self.returned = returned
