# Google_Books_Library

This program allows the user to create a Reading List by searching for books using the Google Books API. It was created exclusively in Python. 

When the user first starts the program, they are greeted with a message and then they have the choice to select one of 3 options.

The first option is to add a new book to the reading list.  If this option is selected, then the program will run a function that allows the user to input the title of the book they are searching for.  That title is then used to search through the Google Books API and prints 5 potential matches.  The user then can select their book if they see the match, but they also have the option to try another search if they can't find the book they are looking for.

The second option is to view the Reading List.  The Reading List is stored in a database that is created by using the Flask extension, Flask-SQLAlchemy.  The database has 3 columns (Title, Author, and Publisher).  Please note that some books in the Google API do not have a publisher listed, so those books will have "N/A" listed as a Publisher.  When the second option is selected, the program will print a list of all the books in the Reading List.

The third option is to shut the program down.  I created a boolean variable called "PROGRAM_ON" that is set to "True".  While this variable is "True", the while loop in the program will keep going.  When the third option is selected, "PROGRAM_ON" will switch to "False" and the program will shutdown.

That should be it for this program.  I hope everyone finds it enjoyable!
