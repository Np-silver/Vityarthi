from src.database import load_data, save_data

def borrow_book(book_id):
    books = load_data()
    for book in books:
        if str(book['book_id']) == str(book_id):
            if book['quantity'] > 0:
                book['quantity'] -= 1
                save_data(books)
                return book  
            else:
                return None 
    return None 