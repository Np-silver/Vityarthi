class Book:
    def __init__(self, book_id, title, author, quantity, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity
        self.price = price
    
    def to_dict(self):
        return self.__dict__

class Transaction:
    def __init__(self, book_id, action):
        import datetime
        self.book_id = book_id
        self.action = action 
        self.timestamp = str(datetime.datetime.now())