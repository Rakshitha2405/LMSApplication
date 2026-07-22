from.book import book
from.member import member

class Library:
    def __init__(self, name: str):
        self.name=name 
        self.books = {}
        self.members = {}

    def add_books(self,book_id,title,author,quantity=1):
        if book_id in self.books: 
            self.books[book_id].quantity+=quantity
        else:
            self.books[book_id]=book(book_id,title,author,quantity)

    def remove_book(self,book_id):
        if book_id in self.books:
            del self.books[book_id]      


    def list_books(self):
        return list(self.books.value())

    def search_books(self,title_query):
        return[
            book for book in self.books.values()
            if title_query.lower() in book.title.lower()
        ]
    
    def add_member(self,member_id,name):
        if member_id not in self.members:
            self.members[member_id]+ member(member_id,name)

    def list_members(self):
        return list(self.members.values())     

    def get_member(self,member_id):
        return self.members.get(member_id) 

    def get_book(self,book_id):
        return self.books.get(book_id) 
    
    def borrow_book(self,member_id,book_id):
        member =self.get_member(member_id)
        book= self.get_book(book_id)

        if not member or not book:
            return False
        
        return member.borrow_book(book)
    
    def return_book(self,member_id,book_id):
        member= self.get_member(member_id)
        book= self.get_book(book_id)

        if not member or not book:
            return False
        
        return member.return_book(book)
 