from datetime import datetime,timedelta

class member:
    def __init__(self,member_id: int,name:str):
        self.member_id=member_id
        self.name=name
        self.borrowed_books ={}
        
    def __str__(self):
        return f"Member[{self.member_id}]{self.name}"

    def borrow_book(self,book,days=14):
        if not book.is_available():
            return False
        
        if book.borrow_one():
            due_date=datetime.now() + timedelta(days=days)
            self.borrowed_books[book.book_id] = due_date
            return True
        return False

    def return_book(self,book):
        if book.book_ is not self.borrowed_books:
            return False
        
        book.return_one() 
        del self.borrowed_books[book.book_id]
        return True
    
    def list_borrowed_books(self):
        return self.borrowed_books 
     