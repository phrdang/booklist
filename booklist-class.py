"""
Welcome to the Book List (Class) project.
Title: booklist-class.py
Author: Rebecca Dang
Date: June 20, 2019
"""

### IMPORT MODULES ###

from time import sleep
from re import findall
from os.path import isfile
from datetime import datetime
from os import listdir

### TROUBLESHOOTING INSTRUCTIONS ###

# Troubleshooting instructions for user for inputting book titles
BOOK_TITLE_TROUBLESHOOT = """
--- BOOK TITLE INPUT TROUBLESHOOTING --

If you're having trouble entering a valid book title, please check the following:

>>> Spelling, capitalization, and spacing 
	DO NOT type: the h8 Ugive
	TYPE: The Hate U Give

>>> Do not include the name of the series 
	DO NOT type: Percy Jackson and the Olympians: The Lightning Thief
	TYPE: The Lightning Thief

>>> Do not include anything besides the title of the book
	DO NOT type: Six of Crows by Leigh Bardugo
	TYPE: Six of Crows

"""

# Troubleshooting instructions for editing a book
EDIT_TROUBLESHOOT = """
--- BOOK EDITING TROUBLESHOOTING ---

>>> If you're having trouble editing a book, it is possible you made a typo while inputting the title of the book.

>>> Follow these instructions:
	1. Choose option 2 of the EDIT BOOK MENU 1.
	2. Choose option 2 of the MAIN MENU.
	3. Choose option 3 of the RETRIEVE INFO menu.
	4. Note down the title of the book you were trying to find.
	5. Choose option 3 of the MAIN MENU. 
	6. Type in the incorrect title that you noted down in Step 3.
	7. Update any incorrect information. 

"""	

# Troubleshooting instructions for retrieving info about a book
RETRIEVE_TROUBLESHOOT = """
--- INFORMATION RETRIEVAL TROUBLESHOOTING ---

>>> If you're having trouble retrieving information about a book, it is possible you made a typo while inputting the title of the book.

>>> Follow these instructions:
	1. Choose option 3 of the RETRIEVE INFO menu.
	2. Note down the title of the book you were trying to find. 
	3. Choose option 3 of the MAIN MENU. 
	4. Type in the incorrect title that you noted down in Step 2.
	5. Update any incorrect information. 

"""

### BOOK CLASS ###

class Book(object):
    id = 0
    titles = []
    authors = []
    genres = []
    tags = []
    series = []

    booklist = {}

    series_dict = {}
    
    def __init__(self, title, author, rating, genres, tags, series):
        '''
        Initializes the book object. 
        title, author: str
        genres, tags: list of str
        rating: int from 1-5
        series: default is None, otherwise str
        '''
        # Saves the user's input with original letter case
        self.title = title
        self.author = author
        self.rating = rating
        self.genres = genres
        self.tags = tags
        self.series = series

        # Unique ID for each book
        Book.id += 1
        self.id = Book.id

        # Saves the user's input except converts it to
        # lower case (only for data types where .lower()
        # works) for case-insensitive searching later on
        self.low_title = title.lower()
        self.low_author = author.lower() 
        self.low_genres = []
        self.low_tags = []
        self.low_series = series.lower()

        for genre in genres:
            self.low_genres.append(genre.lower())
        
        for tag in tags:
            self.low_tags.append(tag.lower())

        # Saves user's input (lowercase) into Book class variables
        # Duplicates are not added
        if title.lower() not in Book.titles:
            Book.titles.append(title.lower())
        
        if author.lower() not in Book.authors:
            Book.authors.append(author.lower())

        for genre in genres:
            if genre.lower() not in Book.genres:
                Book.genres.append(genre.lower())
        
        for tag in tags:
            if tag.lower() not in Book.tags:
                Book.tags.append(tag.lower())

        if series != None and series.lower() not in Book.series:
            Book.series.append(series.lower())

        if series.lower() not in Book.series_dict.keys():
            Book.series_dict[series.lower()] = [self.title, self.low_title]
        
        # Adds all of the book's information onto the Book List
        Book.booklist[self.low_title] = [self.title, [self.author, self.low_author], rating, \
            [self.genres, self.low_genres], [self.tags, self.low_tags], [self.series, self.low_series], self.id]

        '''
        Example Book List dict retrieval:

        Book.booklist['six of crows'] == ['Six of Crows', ['Leigh Bardugo', 'leigh bardugo'], 5, \
            [['YA', 'fantasy'], ['ya', 'fantasy']], [['Kaz', 'Inej', 'Ketterdam'], ['kaz', 'inej', 'ketterdam']], \
                ['Six of Crows Duology', 'six of crows duology'], 1]
        
        TITLE (ORIGINAL)
        Book.booklist['six of crows'][0] == 'Six of Crows'

        AUTHOR (ORIGINAL, LOWER)
        Book.booklist['six of crows'][1] == ['Leigh Bardugo', 'leigh bardugo']

        RATING
        Book.booklist['six of crows'][2] == 5

        GENRES (ORIGINAL, LOWER)
        Book.booklist['six of crows'][3] == [['YA', 'fantasy'], ['ya', 'fantasy']]

        TAGS (ORIGINAL, LOWER)
        Book.booklist['six of crows'][4] == [['Kaz', 'Inej', 'Ketterdam'], ['kaz', 'inej', 'ketterdam']]

        SERIES (ORIGINAL, LOWER) 
        Book.booklist['six of crows'][5] == ['Six of Crows Duology', 'six of crows duology']

        ID 
        Book.booklist['six of crows'][6] == 1
        '''

        # Add book to its series_dict if it belongs to a series
        if self.series != None:
            # If the series is not a key in the dict, create it
            if self.low_series not in Book.series_dict.keys:
                Book.series_dict[self.low_series] = [self.title]
            # Else, if the series already exists, add the new book to the series
            else:
                Book.series_dict[self.low_series].append(self.title)
                
    def __str__(self):
        # First line of info prints the title, author, and rating
        first = 'Title: %s | Author: %s | Rating: %s' % (self.title, self.author, self.rating)
        
        # Converts the self.genres list to a readable str
        genres_str = ''
        for genre in self.genres:
            if self.genres[-1] == genre:
                genres_str += genre
            else:
                genres_str += genre + ', '

        # Converts the self.tags list to a readable str
        tags_str = ''
        for tag in self.tags:
            if tags[-1] == tag:
                tags_str += tag
            else:
                tags_str += tag + ', '

        # Second line of info prints the series (if it has one), genres, and tags
        if self.series == None:
            second = '\nGenre(s): %s | Tag(s): %s' % (genres_str, tags_str)
        else: 
            # Second line of info prints the genres and tags
            second = '\nSeries: %s | Genre(s): %s | Tag(s): %s' % (self.series, genres_str, tags_str)

        # Third line of info prints the book ID
        third = '\nID: ' + str(self.id)
        
        return first + second + third

    ### GETTER METHODS ###

    def get_title(self):
        '''
        Returns: title of book, a str
        '''
        return self.title
    
    def get_author(self):
        '''
        Returns: author of book, a str
        '''
        return self.author

    def get_rating(self):
        '''
        Returns: rating of book, an int from 1-5
        '''
        return self.rating
    
    def get_genres(self):
        '''
        Returns: genre(s) of book, a list
        '''
        return self.genres
    
    def get_tags(self):
        '''
        Returns: tag(s) of book, a list
        '''
        return self.tags

    def get_series(self):
        '''
        Returns: series of book, a str
        '''
        return self.series

    def get_id(self):
        '''
        Returns: ID of book, an int
        '''
        return self.id

    ### SETTER METHODS ###

    def set_title(self, new_title):
        '''
        new_title: str
        Sets self.title
        '''
        self.title = new_title
    
    def set_author(self, new_author):
        '''
        new_author: str
        Sets self.author
        '''
        self.author = new_author

    def set_rating(self, new_rating):
        '''
        new_rating: int from 1-5
        Sets self.rating
        '''
        self.rating = new_rating
    
    def set_genres(self, new_genres):
        '''
        new_genres: list of str
        Sets self.genres
        '''
        self.genres = new_genres
    
    def set_tags(self, new_tags):
        '''
        new_tags: list of str
        Sets self.tags
        '''
        self.tags = new_tags

    def set_series(self, new_series):
        '''
        new_series: str
        Sets self.series
        '''
        self.series = new_series

### FUNCTIONS ###

'''
def title_input(purpose):
	Asks user for title of a book

	purpose: str, the purpose of the function ('retrieve', 'edit', or 'add')

	Returns: str, title of book from user input, formatted in a way so that the program can use the information
	 
'''

def title_input(purpose):
    '''
    Asks user for title of a book

    purpose: str, the purpose of the function ('retrieve', 'edit', or 'add')

    Returns: str, title of book from user input, formatted
    in a way so that the program can use the information
    '''

    issue_counter = 0

    while True:
        # Asks user for the title of the book
        title = input("Title: ")

        # Checks if the title starts with the string 'The', then moves 'The' to the back of the title.
        # This is for alphabetizing purposes. 
        if title[:3] == "The":
            title = title[4:] + ", The"

        # Checks if user has inputted anything
        if not title:
            print("Sorry, you did not enter a title of the book.")
            print()
        
        if purpose == 'retrieve' or purpose == 'edit':
            # Error message if book the user wants to retrieve info about or edit does not exist
            if title.lower() not in Book.titles:
                print('Sorry, book not found in the Book List. Please type in the title of an EXISTING book.')
                sleep(1)
                print()
                issue_counter += 1
                # Only prints the long troubleshooting instructions if this is the 3rd time
                # the user is having trouble (otherwise it gets annoying)
                if issue_counter == 3:
                    # Prints out instructions on how to correctly type in a book title 
                    # if book doesn't exist in booklist
                    for line in BOOK_TITLE_TROUBLESHOOT.splitlines():
                        print(line)
                        sleep(0.3)
                    if purpose == 'retrieve':
                        # Prints out retrieve troubleshoot instructions
                        for line in RETRIEVE_TROUBLESHOOT.splitlines():
                            print(line)
                            sleep(0.3)
                    elif purpose == 'edit':
                        # Prints out edit troubleshoot instructions
                        for line in EDIT_TROUBLESHOOT.splitlines():
                            print(line)
                            sleep(0.3)
            # If the book does exist, exit while loop
            else:
                break

        # If user tries to enter a title that already exists in the Book List
        # Program will alert user to confirm whether they want to complete
        # this action (because it might be same title diff author)
        if purpose == 'add' and title.lower() in Book.titles:
                for book in booklist:
                    if book.get_title() == title:
                        author = book.get_author()
                        id = book.get_id()
                print("This book title already exists in the Book List: %s by %s. ID: %d" % (title, author, id))
                print("Are you trying to add a book by a different author with the same title?")

                while True:
                    try:
                        user_input = input("Y or N: ")
                        assert user_input.lower() == 'y' or user_input.lower() == 'n'
                    except AssertionError:
                        print("Error, please enter Y or N.")
                    else:
                        if user_input == 'y':
                            print("You said YES. The title you inputted has been recorded.")
                        else:
                            print("You said NO. Please enter a different title.")
                        break
                
                if user_input == 'y':
                    break

        # If book is a new book, exit while loop
        else:
            break

    return title

def author_input():
	'''
	Asks user for name of an author of a book

	Returns: str, name of author inputted
	'''

	while True:
		# Asks user for the author of the book
		author = input("Author: ")
		# Checks if user has inputted anything
		if not author:
			print("Sorry, you did not enter an author of the book.")
		else:
			return author

def rating_input():
	'''
	Asks user for rating of a book

	Returns: rating, an int from 1-5
	'''

	while True:
		try:
			rating = int(input("Rating (out of 5 stars): "))
			# User input cannot be empty and rating must be an integer from 1-5 
			assert rating and rating <= 5 and rating >= 1
		except ValueError:
			print("Error, please enter an integer.")
		except AssertionError:
			print("Error, please enter an integer between 1 and 5.")
		else:
			return rating

def series_input():
	'''
	Asks user for name of the series of a book

	Returns: str, name of series inputted
	'''

	while True:
		# Asks user for the series of the book
		series = input("Series: ")
		# Checks if user has inputted anything
		if not series:
			print("Sorry, you did not enter the series of the book.")
		else:
			return series

def genres_input():
    '''
    Asks user for the genres of a book

    Returns: list of str, genres
    '''
    genres = []
    genre_counter = 0

    # Asks user for the genre(s) of the book
    print("What genre(s) does your book fall under? Enter ONE genre at a time. \
Once you are done, type in 'd' and press Enter.")

    while True:
        genre_counter += 1
        genre = input("Genre #%d: " % (genre_counter))
        if not genre:
            print("Sorry, you did not enter a genre of the book.")
        elif genre.lower() == 'd':
            # Checks if the user has entered at least 1 genre, if not
            # while loop continues
            if genres:
                return genres
            else:
                print("Sorry, you did not enter any genre(s) for this book.\
Please enter at least 1 genre.")
                genre_counter = 0
        else:
            genres.append(genre)
        
        

def tags_input():
    '''
    Asks user for the tags of a book

    Returns: list of str, tags
    '''
    tags = []
    tag_counter = 0

    # Asks user for the tag(s) of the book
    print("What is your book tagged as? This will help with searching for books. \
Enter ONE tag at a time. Once you are done, type in 'd' and press Enter.")

    while True:
        tag_counter += 1
        tag = input("Tag #%d: " % (tag_counter))
        if not tag:
            print("Sorry, you did not enter a tag for the book.")
        elif tag.lower() == 'd':
            # Checks if the user has entered at least 1 tag, if not
            # while loop continues
            if tags:
                return tags
            else:
                print("Sorry, you did not enter any tag(s) for this book.\
Please enter at least 1 tag.")
                tag_counter = 0
        else:
            tags.append(tag)

def new_book():
    '''
	Takes in user input to create a new Book object

	Returns: None
    '''
    print('You have chosen option 1, to add a new book.')

    while True:
        # Asks the user for the title, author, and rating.
        title = title_input('add')
        author = author_input()
        rating = rating_input()

        # Asks user if the book is part of a series, and if it is,
        # asks user to input the series name
        while True:
            try:
                user_input = input('''Is this book part of a series?
        (Y) Yes
        (N) No
Y or N: ''').lower()
                assert user_input.lower() == 'y' or user_input.lower() == 'n'
            except AssertionError:
                print("Error, please enter Y or N.")
            else:
                if user_input == 'y':
                    series = series_input()
                else:
                    series = None
                break
        
        # Asks the user for the genres and tags
        genres = genres_input()
        tags = tags_input()

        # Converts the self.genres list to a readable str
        genres_str = ''
        for genre in genres:
            if genres[-1] == genre:
                genres_str += genre
            else:
                genres_str += genre + ', '

        # Converts the self.tags list to a readable str
        tags_str = ''
        for tag in tags:
            if tags[-1] == tag:
                tags_str += tag
            else:
                tags_str += tag + ', '

        # Asks the user to confirm that the inputted info is correct
        print()
        print()
        print("Is this correct?")
        print()
        print("Title:", title)
        print("Author:", author)
        print("Rating:", rating)
        print("Series:", series)
        print("Genres:", genres_str)
        print("Tags:", tags_str)
        print()

        user_input = input("Y or N: ").lower()

        # If the user confirms that it's correct then a new Book object
        # is created and a confirmation is displayed.
        if user_input == 'y':
            book = Book(title, author, rating, genres, tags, series)
            booklist.append(book)
            sleep(1)
            print("The book %s by %s has been added." % (title.upper(), author.upper()))
            break
        # Else, the program prompts the user to re-enter their information
        else:
            print("Please enter your information again.")

### TEST CODE ###

# booklist = []

title = 'Six of Crows'
author = 'Leigh Bardugo'
rating = 5
genres = ['YA', 'Fantasy']
tags = ['kaz brekker', 'inej ghafa', 'ketterdam']
series = 'Six of Crows Duology'
soc_obj = Book(title, author, rating, genres, tags, series)
booklist.append(soc_obj)

title = 'Crooked Kingdom'
author = 'Leigh Bardugo'
rating = 4
genres = ['YA', 'Fantasy']
tags = ['kaz brekker']
series = 'Six of Crows Duology'
ck_obj = Book(title, author, rating, genres, tags, series)
booklist.append(ck_obj)

title = 'Heartless'
author = 'Marissa Meyer'
rating = 3
genres = ['YA', 'Fantasy', 'Romance']
tags = ['alice', 'in', 'wonderland']
series = None
hl_obj = Book(title, author, rating, genres, tags, series)
booklist.append(hl_obj)


for book in booklist:
    print(book)

print(Book.titles)
print(Book.authors)
print(Book.genres)
print(Book.tags)
print(Book.series)