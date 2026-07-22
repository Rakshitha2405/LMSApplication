class book:
    def __init__(self,book_id: int, title: str, author:str, quantity: int=1):
        self.book_id=book_id
        self.title=title
        self.author=author 
        self.quality=self.quality
        
    def __str__(self):
       return f"[{self.book_id}] {self.title} by {self.author} (Available: {self.quality})" 

    def is_available(self):
       return self.quality > 0
    
    def borrow_one(self):
       if self.is_available():
          self.quality -= 1
          return True   
       return False
    def return_one(self):
        self.quality += 1