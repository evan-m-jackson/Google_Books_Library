import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

endpoint = "https://www.googleapis.com/books/v1/volumes"
PROGRAM_ON = True

#CREATES A READING LIST DATABASE
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reading-list.db'
db = SQLAlchemy(app)

#CREATES DATABASE COLUMNS
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    author = db.Column(db.String(250))
    publisher = db.Column(db.String(250))

    def __repr__(self):
        return f'Title: {self.title} | Author: {self.author} | Publisher: {self.publisher}'

db.create_all()

#FUNCTION TO SEARCH FOR A BOOK IN GOOGLE API
def find_a_book():
    title = input("Please enter the book you are looking for: ")
    params = {
        "q": title,
        "orderBy": "relevance",
        "maxResults": 5,
    }

    response = requests.get(url=f"{endpoint}", params=params)
    response.raise_for_status()
    data = response.json()
    book_list = data['items']

    book_dict = {}
    count = 0

    for books in book_list:
        count += 1
        title = books['volumeInfo']['title']
        author = books['volumeInfo']['authors'][0]
        #Some books do not have publishers, so they will get an N/A instead
        try:
            publisher = books['volumeInfo']['publisher']
        except:
            publisher = 'N/A'
        book_dict[str(count)] = {'title': title, 'author': author, 'publisher': publisher}
        print(f"{count} Title: {title} | Authors: {author} | Publisher: {publisher}")

    book_choice = input("\nPlease choose your book (Enter 1-5).  If you don't see your book then enter 0: ")
    if book_choice == '0':
        print("Couldn't find it? Maybe try a more specific title?")
        find_a_book()
    elif int(book_choice) >= 1 and int(book_choice) <= 5:
        my_book = book_dict[book_choice]

        book_to_add = Book(title=my_book['title'], author=my_book['author'], publisher=my_book['publisher'])
        db.session.add(book_to_add)
        db.session.commit()
    else:
        print("Please enter a number between 0 and 5.")
        find_a_book()

#OPENING GREETING LINE
print("Welcome to your personal library!")

while PROGRAM_ON:
    greeting = input("Please select an option: \nPress '1' to add a book\nPress '2' to view your library\nPress '3' to exit the program\n")

    if greeting == '1':
        find_a_book()

    elif greeting == '2':
        all_books = Book.query.all()
        print(all_books)

    elif greeting == '3':
        PROGRAM_ON = False

    else:
        print("Please select 1, 2, or 3.")










