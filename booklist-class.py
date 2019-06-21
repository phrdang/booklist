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
    def __init__(self, title, author, rating, genres, tags, series=None):
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

### TEST CODE ###
title = 'Six of Crows'
author = 'Leigh Bardugo'
rating = '5'
genres = ['YA', 'Fantasy']
tags = ['kaz brekker', 'inej ghafa', 'ketterdam']
series = 'Six of Crows Duology'
soc_obj = Book(title, author, rating, genres, tags, series)
print(soc_obj)