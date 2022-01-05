# Google_Books_Library #

This program allows the user to create a Reading List by searching for books using the Google Books API. It was created exclusively in Python. 

It is highly recommended that the user has the latest version of Python installed.  It can be downloaded from this link: https://www.python.org/downloads/.


# Getting Started #

On the main page for the Google_Reading_List repository, click on the green "Code" button in the upper right hand corner.  Then click on "Download ZIP" from the drop-down menu.  After the zip file is finished downloading, select "Open" and then move the unzipped file from the "Downloads" folder into the "Desktop" folder.

Next, open a Terminal window (please note I'm using Mac OS) and enter the following 2 commands:
  
    cd Desktop
  
    cd Google_Reading_List-main

After that, the next 3 lines will need to be entered to add the required packages (please see the "requirements.txt" file in the "Google_Reading_List-main" folder for more details on the packages):

    pip install requests
  
    pip install flask
  
    pip install flask-sqlalchemy
  
Finally, enter the following to run the code:
  
    python3 main.py
  
In addition, there is a test file that can be run by entering:

    python3 test_main.py
  

# How it Works #  
  
When the user first starts the program, they are greeted with a message and then they have the choice to select one of 3 options.

The first option is to add a new book to the reading list.  If this option is selected, then the program will run a series of functions that allows the user to input the title of the book they are searching for.  That title is then used to search through the Google Books API and prints 5 potential matches.  The user then can select their book if they see the match, but they also have the option to try another search if they can't find the book they are looking for.

The second option is to view the Reading List.  The Reading List is stored in a database that is created by using the Flask extension, Flask-SQLAlchemy.  The database has 3 columns (Title, Author, and Publisher).  Please note that some books in the Google API do not have a publisher listed, so those books will have "N/A" listed as a Publisher.  When the second option is selected, the program will print a list of all the books in the Reading List.

The third option is to shut the program down.  I created a boolean variable called "PROGRAM_ON" that is set to "True".  While this variable is "True", the while loop in the program will keep going.  When the third option is selected, "PROGRAM_ON" will switch to "False" and the program will shutdown.

That should be it for this program.  I hope everyone finds it enjoyable!
