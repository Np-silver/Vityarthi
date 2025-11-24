import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.models import Book

class TestBookModels(unittest.TestCase):
    
    def test_book_creation(self):
        book = Book("101", "Python Guide", "Guido", 10, 29.99)
        
        self.assertEqual(book.title, "Python Guide")
        self.assertEqual(book.quantity, 10)
        self.assertEqual(book.price, 29.99)

    def test_to_dict(self):
        book = Book("102", "Clean Code", "Uncle Bob", 5, 40.00)
        data = book.to_dict()
        
        self.assertIsInstance(data, dict)
        self.assertEqual(data['author'], "Uncle Bob")
        self.assertEqual(data['price'], 40.00)

if __name__ == '__main__':
    unittest.main()