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
    def __init__(self, title, author, rating, genres, tags, series):
        '''
        Initializes the book object. 
        title, author: str
        genres, tags: list of str
        rating: int from 1-5
        series: default is None, otherwise str
        '''
        self.title = title
        self.author = author
        self.rating = rating
        self.genres = genres
        self.tags = tags
        self.series = series

        Book.id += 1
        self.id = Book.id

        # Add the new book's info to the overall pool of info
        # which is stored in the Book class variables
        # Check if the new info already exists in those lists
        # If don't already exist, add them to the lists

        Book.titles.append(title)

        if author not in Book.authors:
            Book.authors.append(author)

        # Both genre and tag iterate to prevent lists inside of lists
        for genre in genres:
            if genre not in Book.genres:
                Book.genres.append(genre)

        for tag in tags:
            if tag not in Book.tags:
                Book.tags.append(tag)

        if series not in Book.series:
            Book.series.append(series)

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

def title_input(purpose):
	'''
	Asks user for title of a book

	purpose: str, the purpose of the function ('retrieve', 'edit', or 'add')

	Returns: str, title of book from user input, formatted in a way so that the program can use the information
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
		# Else block runs if user has inputted something
		else:
			if purpose == 'retrieve' or purpose == 'edit':
				# Error message if book the user wants to retrieve info about or edit does not exist
				if title not in Book.titles:
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

			# If block runs if user tries to create a new book that already exists in the Book List
			if purpose == 'add' and title in Book.titles:
				print("Sorry, this book already exists in the Book List. Please type in the title of a NEW book.")
				sleep(1)
				print()
				issue_counter += 1
				# Only prints the long troubleshooting instructions if this is the first time
				# the user is having trouble (otherwise it gets annoying)
				if issue_counter == 3:
					# Prints out instructions on how to correctly type in a book title 
					# if book already exists in booklist
					for line in BOOK_TITLE_TROUBLESHOOT.splitlines():
						print(line)
						sleep(0.3)
			# If book is a new book, exit while loop
			elif purpose == 'add' and title not in Book.titles:
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
            break
        else:
            genres.append(genre)

    return genres

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
            break
        else:
            tags.append(tag)

    return tags

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
        # Any character besides "y" or "Y" is considered "No"
        user_input = input('''Is this book part of a series?
        (Y) Yes
        (N) No
Y or N: ''').lower()
        if user_input == 'y':
            series = series_input()
        else:
            series = None
        
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

booklist = []

### TEST CODE ###
title = 'Six of Crows'
author = 'Leigh Bardugo'
rating = '5'
genres = ['YA', 'Fantasy']
tags = ['kaz brekker', 'inej ghafa', 'ketterdam']
series = 'Six of Crows Duology'
soc_obj = Book(title, author, rating, genres, tags, series)
# print(soc_obj)

new_book()
print("Enter book #2")
new_book()
for book in booklist:
    print(book)