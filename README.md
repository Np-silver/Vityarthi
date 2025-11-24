BookKeeper - Library Management System

Overview
 
BookKeeper is a robust, modular Python application designed to help librarians manage book inventories efficiently. It simplifies the core operations of a library, including adding new stock, tracking book availability, managing book removal, and processing customer checkouts with real-time price calculation.

This project was built to demonstrate Modular Architecture, CRUD Operations, and Data Persistence using Python.

Key Features

Inventory Management: Add new books with detailed attributes (Title, Author, Quantity, Price).

Search & Filtering: Instantly search for books by title with a formatted table view.

Stock Control: "Checkout" functionality automatically reduces stock quantity and calculates the total price.

Data Persistence: All data is saved locally to data/books.json, ensuring no data is lost when the app closes.

Maintenance: Safe deletion of obsolete books from the system.

Robust Error Handling: Validates user inputs (e.g., prevents entering text for prices).

Technologies Used

Language: Python 3.10+

Data Storage: JSON (File Handling)

Testing: Python unittest framework

Interface: Command Line Interface (CLI)

Project Structure

BookKeeper/
├── data/
│   └── books.json          
├── src/
│   ├── __init__.py
│   ├── models.py           
│   ├── database.py         
│   ├── inventory.py        
│   ├── lending.py          
│   └── utils.py            
├── tests/
│   └── test_models.py      
├── main.py                
└── README.md               

Steps to Install & Run

Prerequisites: Ensure you have Python installed.

python --version

Download the Project: Download the zip file or clone the repository to your local machine.

Navigate to the Folder: Open your terminal/command prompt and cd into the project directory.

cd BookKeeper

Run the Application: Execute the main script to start the CLI.

python main.py

Download the Project:
Download the zip file or clone the repository to your local machine.

Navigate to the Folder:
Open your terminal/command prompt and cd into the project directory.

cd BookKeeper

Run the Application:
Execute the main script to start the CLI.

python main.py

Instructions for Testing

This project includes automated unit tests to verify the integrity of the Data Models.

To run the test suite:

Open your terminal in the BookKeeper folder.

Run the following command:

python -m unittest discover tests

You should see an output indicating OK if all tests pass.

Screenshots

Main Menu:

BookKeeper
[1] Add New Book 
[2] Search Inventory 
[3] Delete Book 
[4] Checkout / Borrow
[5] Exit

Search Results:
ID TITLE AUTHOR QTY PRICE

101 Python Crash Course Eric Matthes 5 $29.99

102 Clean Code Robert C. Martin 3 $45.50

You should see an output indicating OK if all tests pass.

