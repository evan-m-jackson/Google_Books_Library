import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

endpoint = "https://www.googleapis.com/books/v1/volumes"
PROGRAM_ON = True

# CREATES A READING LIST DATABASE
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///reading-list.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# CREATES DATABASE COLUMNS
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    author = db.Column(db.String(250))
    publisher = db.Column(db.String(250))

    def __repr__(self):
        return (
            f"Title: {self.title} | Author: {self.author} | Publisher: {self.publisher}"
        )


# THIS CAN BE HIDDEN AFTER FIRST RUN
db.create_all()


def get_search_item():
    title = input("Please enter the book you are looking for: ")
    return title

#CREATES PARAMETERS FOR API CALL
def get_params(title):
    params = {
        "q": title,
        "orderBy": "relevance",
        "maxResults": 5,
    }
    return params

#GOOGLE BOOKS API CALL
def get_book_list(params):
    response = requests.get(url=f"{endpoint}", params=params)
    response.raise_for_status()
    data = response.json()
    book_list = data["items"]
    return book_list

def get_title(book):
    title = book["volumeInfo"]["title"]
    return title

#FUNCTION ONLY TAKES FIRST AUTHOR IN CASE THERE ARE MULTIPLE. ALSO RETURNS N/A IF NO AUTHOR EXISTS FOR THE SEARCHED BOOK
def get_author(book):
    try:
        author = book["volumeInfo"]["authors"][0]
    except:
        author = "N/A"
    return author

#RETURNS N/A IF NO PUBLISHER EXISTS FOR THE SEARCHED BOOK
def get_publisher(book):
    try:
        publisher = book["volumeInfo"]["publisher"]
    except:
        publisher = "N/A"
    return publisher

#PRINTS LIST OF BOOKS TO CHOOSE FROM BASED ON SEARCH TERM, AS WELL AS RETURNING A DICTIONARY OF THE SEARCHED BOOK LIST
def get_book_choices(list_):
    book_dict = {}
    count = 0
    for book in list_:
        count += 1
        title = get_title(book)
        author = get_author(book)
        publisher = get_publisher(book)
        book_dict[str(count)] = {
            "title": title,
            "author": author,
            "publisher": publisher,
        }
        print(f"{count} Title: {title} | Authors: {author} | Publisher: {publisher}")
    return book_dict

def get_user_selection():
    book_choice = input(
        "\nPlease choose your book (Enter 1-5).  If you don't see your book then hit any key: "
    )
    return book_choice

#USES THE RETURNED DICTIONARY FROM GET_BOOK_CHOICES AND RETURNED INPUT FROM GET_USER SELECTION AS PARAMETERS TO ADD A NEW BOOK TO THE DATABASE (I.E. THE LIBRARY)
def add_book(book_dict, choice):
    my_book = book_dict[choice]
    book_to_add = Book(
        title=my_book["title"],
        author=my_book["author"],
        publisher=my_book["publisher"],
    )
    db.session.add(book_to_add)
    db.session.commit()
    print(f"{my_book['title']} has been added to the library.")

#IF THE USER DOESN'T MAKE A SELECTION FROM THE LIST OF BOOKS
def no_book():
    print("Couldn't find it? Maybe try a more specific title?")

#MAIN FUNCTION TO RUN ALL ABOVE SINGLE RESPONSIBILITY FUNCTIONS
def find_a_book():
    search = get_search_item()

    parameters = get_params(search)

    book_list = get_book_list(parameters)

    book_dict = get_book_choices(book_list)

    choice = get_user_selection()

    try:
        if int(choice) >= 1 and int(choice) <= 5:
            add_book(book_dict, choice)
        else:
            no_book()
            find_a_book()
    except:
        no_book()
        find_a_book()

# OPENING GREETING LINE
print("Welcome to your personal library!")

# PROGRAM START
while PROGRAM_ON:
    greeting = input(
        "Please select an option: \nPress '1' to add a book\nPress '2' to view your library\nPress '3' to exit the program\n"
    )

    if greeting == "1":
        find_a_book()

    elif greeting == "2":
        all_books = Book.query.all()
        print(all_books)

    elif greeting == "3":
        PROGRAM_ON = False

    else:
        print("Please select 1, 2, or 3.")
