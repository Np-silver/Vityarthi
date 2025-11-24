import sys
from src.models import Book
from src.inventory import add_book, search_book, remove_book
from src.lending import borrow_book

def header():
    print()
    print("BookKeeper")
    print()

def menu():
    print("[1] Add New Book")
    print("[2] Search Inventory")
    print("[3] Delete Book")
    print("[4] Checkout / Borrow")
    print("[5] Exit")
    print()

def add():
    print(" Add New Book ")
    
    bid = input("Enter Book ID: ")
    if not bid: return
    
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    
    qty_str = input("Enter Quantity: ")
    price_str = input("Enter Price ($): ")
    
    is_valid_qty = qty_str.isdigit()
    is_valid_price = price_str.replace('.', '', 1).isdigit()
    
    if is_valid_qty and is_valid_price:
        qty = int(qty_str)
        price = float(price_str)
        
        new_book = Book(bid, title, author, qty, price)
        add_book(new_book)
        print("Success: added to inventory.")
    else:
        print("Quantity must be an integer and Price must be a number.")

def search():
    print(" Search Inventory ")
    keyword = input("Search by Title (or press Enter for all): ")
    results = search_book(keyword)
    
    if not results:
        print("No books found.")
        return

    
    print("ID".ljust(6) + " " + "TITLE".ljust(30) + " " + "AUTHOR".ljust(20) + " " + "QTY".ljust(5) + " " + "PRICE".ljust(8))
    print("-" * 75)
    
    for b in results:
        price = b.get('price', 0.0)
    
        p_rounded = round(price, 2)
        p_str = str(p_rounded)
        if "." in p_str:
            
            if len(p_str.split(".")[1]) == 1:
                p_str += "0"
        else:
            
            p_str += ".00"

        print(str(b['book_id']).ljust(6) + " " + 
              b['title'][:28].ljust(30) + " " + 
              b['author'][:18].ljust(20) + " " + 
              str(b['quantity']).ljust(5) + " $" + 
              p_str.ljust(8))

def delete(): 
    print(" Delete Book ")
    search()
    
    bid = input("Based on the list above, enter ID to DELETE: ")
    if not bid: return

    confirm = input("Are you sure you want to delete ID ? (y/n): ")
    if confirm.lower() == 'y':
        if remove_book(bid):
            print("Book  deleted successfully.")
        else:
            print("Book ID  not found.")

def borrow():
    print(" Checkout Desk ")
    bid = input("Enter Book ID to checkout: ")

    book = borrow_book(bid)
    
    if book:
        price = book.get('price', 0.0)
        
    
        p_rounded = round(price, 2)
        p_str = str(p_rounded)
        if "." in p_str:
            if len(p_str.split(".")[1]) == 1:
                p_str += "0"
        else:
            p_str += ".00"

        print(" CHECKOUT SUCCESSFUL")
        print("*"*30)
        
        print("Item:  " + str(book['title']))
        print("Price: $" + p_str)
        print("*"*30)
    else:
        print(" Book not found or Out of Stock.")

def main():
    header()
    while True:
        menu()
        choice = input("Select Option: ")
        
        if choice == '1':
            add()
        elif choice == '2':
            search()
        elif choice == '3':
            delete()
        elif choice == '4':
            borrow()
        elif choice == '5':
            print("Exiting system. Goodbye!")
            sys.exit()
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()