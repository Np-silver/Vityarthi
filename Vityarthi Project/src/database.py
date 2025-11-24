import json
import os
import configparser

config = configparser.ConfigParser()
config.read('settings.cfg')

try:
    DATA_FILE = config['Storage']['db_path']
except KeyError:
    DATA_FILE = 'data/books.json'


DEFAULT_BOOKS = [

    {"book_id": "101", "title": "Python Crash Course", "author": "Eric Matthes", "quantity": 12, "price": 29.99},
    {"book_id": "102", "title": "Clean Code", "author": "Robert C. Martin", "quantity": 8, "price": 45.50},
    {"book_id": "103", "title": "The Pragmatic Programmer", "author": "Andrew Hunt", "quantity": 6, "price": 39.95},
    {"book_id": "104", "title": "Introduction to Algorithms", "author": "Thomas Cormen", "quantity": 4, "price": 85.00},
    {"book_id": "105", "title": "Design Patterns", "author": "Erich Gamma", "quantity": 5, "price": 49.99},
    {"book_id": "106", "title": "You Don't Know JS", "author": "Kyle Simpson", "quantity": 10, "price": 25.00},
    {"book_id": "107", "title": "Automate the Boring Stuff", "author": "Al Sweigart", "quantity": 15, "price": 24.95},
    {"book_id": "108", "title": "Fluent Python", "author": "Luciano Ramalho", "quantity": 7, "price": 40.00},
    {"book_id": "109", "title": "Head First Java", "author": "Kathy Sierra", "quantity": 9, "price": 35.00},
    {"book_id": "110", "title": "Cracking the Coding Interview", "author": "Gayle Laakmann", "quantity": 20, "price": 32.50},
    
    
    {"book_id": "201", "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "quantity": 15, "price": 12.99},
    {"book_id": "202", "title": "The Hobbit", "author": "J.R.R. Tolkien", "quantity": 12, "price": 14.99},
    {"book_id": "203", "title": "1984", "author": "George Orwell", "quantity": 25, "price": 9.99},
    {"book_id": "204", "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "quantity": 18, "price": 10.50},
    {"book_id": "205", "title": "To Kill a Mockingbird", "author": "Harper Lee", "quantity": 20, "price": 11.99},
    {"book_id": "206", "title": "The Catcher in the Rye", "author": "J.D. Salinger", "quantity": 10, "price": 10.00},
    {"book_id": "207", "title": "Dune", "author": "Frank Herbert", "quantity": 8, "price": 18.00},
    {"book_id": "208", "title": "The Fellowship of the Ring", "author": "J.R.R. Tolkien", "quantity": 10, "price": 15.50},
    {"book_id": "209", "title": "Pride and Prejudice", "author": "Jane Austen", "quantity": 14, "price": 8.99},
    {"book_id": "210", "title": "The Alchemist", "author": "Paulo Coelho", "quantity": 22, "price": 13.00},

    
    {"book_id": "301", "title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "quantity": 11, "price": 19.99},
    {"book_id": "302", "title": "A Brief History of Time", "author": "Stephen Hawking", "quantity": 9, "price": 16.50},
    {"book_id": "303", "title": "Thinking, Fast and Slow", "author": "Daniel Kahneman", "quantity": 7, "price": 17.00},
    {"book_id": "304", "title": "Quiet", "author": "Susan Cain", "quantity": 6, "price": 14.00},
    {"book_id": "305", "title": "The Power of Habit", "author": "Charles Duhigg", "quantity": 13, "price": 15.00},
    {"book_id": "306", "title": "Atomic Habits", "author": "James Clear", "quantity": 30, "price": 22.00},
    {"book_id": "307", "title": "Educated", "author": "Tara Westover", "quantity": 10, "price": 16.00},
    {"book_id": "308", "title": "Becoming", "author": "Michelle Obama", "quantity": 15, "price": 18.50},
    {"book_id": "309", "title": "Cosmos", "author": "Carl Sagan", "quantity": 5, "price": 19.00},
    {"book_id": "310", "title": "Outliers", "author": "Malcolm Gladwell", "quantity": 12, "price": 14.50},

    
    {"book_id": "401", "title": "The Da Vinci Code", "author": "Dan Brown", "quantity": 14, "price": 12.50},
    {"book_id": "402", "title": "Gone Girl", "author": "Gillian Flynn", "quantity": 9, "price": 13.00},
    {"book_id": "403", "title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson", "quantity": 11, "price": 14.00},
    {"book_id": "404", "title": "Sherlock Holmes: Complete", "author": "Arthur Conan Doyle", "quantity": 8, "price": 25.00},
    {"book_id": "405", "title": "And Then There Were None", "author": "Agatha Christie", "quantity": 16, "price": 10.99},

    
    {"book_id": "501", "title": "The Very Hungry Caterpillar", "author": "Eric Carle", "quantity": 20, "price": 8.50},
    {"book_id": "502", "title": "Green Eggs and Ham", "author": "Dr. Seuss", "quantity": 18, "price": 9.00},
    {"book_id": "503", "title": "Charlotte's Web", "author": "E.B. White", "quantity": 15, "price": 7.99},
    {"book_id": "504", "title": "Diary of a Wimpy Kid", "author": "Jeff Kinney", "quantity": 25, "price": 11.50},
    {"book_id": "505", "title": "Watchmen", "author": "Alan Moore", "quantity": 7, "price": 22.00},
    {"book_id": "506", "title": "Maus", "author": "Art Spiegelman", "quantity": 6, "price": 19.99},
    {"book_id": "507", "title": "Persepolis", "author": "Marjane Satrapi", "quantity": 5, "price": 18.00},
    {"book_id": "508", "title": "Calvin and Hobbes", "author": "Bill Watterson", "quantity": 10, "price": 21.00},
    {"book_id": "509", "title": "Where the Wild Things Are", "author": "Maurice Sendak", "quantity": 14, "price": 9.50},
    {"book_id": "510", "title": "Matilda", "author": "Roald Dahl", "quantity": 12, "price": 8.99}
]

def load_data():
    
    if not os.path.exists(DATA_FILE):
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        save_data(DEFAULT_BOOKS)
        return DEFAULT_BOOKS

    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            if not data: return DEFAULT_BOOKS
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return DEFAULT_BOOKS

def save_data(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)