from src.database import load_data, save_data

def add_book(book_obj):
    books = load_data()
    books.append(book_obj.to_dict())
    save_data(books)

def search_book(keyword):
    books = load_data()
    if not keyword:
        return books
    return [b for b in books if keyword.lower() in b['title'].lower()]

def remove_book(book_id):
    books = load_data()
    initial_count = len(books)
    books = [b for b in books if str(b['book_id']) != str(book_id)]
    
    if len(books) < initial_count:
        save_data(books)
        return True
    return False
