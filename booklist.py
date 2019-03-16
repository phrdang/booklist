"""
Welcome to the Book List project.
Title: booklist.py
Author: Rebecca Dang
Date: September 27, 2018
This program is intended to:
1. Take in the following inputs from the user: 
	-Book Title
	-Author
	-Rating (out of 5 stars)
2. Organize the inputs into separate dictionaries
3. Be able to retrieve values from keys in the dictionaries
4. Output any desired information to the user:
	-The author of a book
	-The rating of a book
	-List of all books in the list

INSTRUCTIONS FOR USE OF THIS PROGRAM VIA THE MAC TERMINAL:
1. Open Terminal from Spotlight search.
2. cd into wherever you saved the booklist.py file
3. Type in python3 booklist.py

UPDATE: September 29, 2018
All original objectives have been fulfilled, and extensive testing has been successful.
Adding Objective 5: Allow the user to edit previously inputted information. 

UPDATE: September 29, 2018
All 5 objectives have been fulfilled, and extensive testing has been successful.

UPDATE: September 29, 2018
Testing by Mom and Dad has generated some errors! Time to fix.

UPDATE: September 30, 2018
Fixed errors brought up by parents testing yesterday. Updated credits and other features.

UPDATE: March 10, 2019
NEW ADDITIONAL OBJECTIVES:
1. Use try, except
2. Be able to write and read .txt files for booklist
3. Use book class

UPDATE: March 13, 2019
-Currently working on N.A.O. #1
-Don't forget to merge try-except branch with master once finished!
NEW ADDITIONAL OBJECTIVES:
4. Update retrieve_rating and retrieve_author
	-Combine helper functions into one retrieve function
	-Move troublingshooting instructions and check if book in book_list_dict into that retrieve function
	to avoid repetitive code
5. Make print_all_books more aesthetic
6. Once classes implemented:
	-Book IDs
	-Genres
	-Avg. rating function for genre, author
	-CLASSES (by inheritance?):
		-Book
			-Author?
			-Genre?
7. ADD DOCSTRINGS

UPDATE: March 14, 2019
NEW ADDITIONAL OBJECTIVES:
8. Make user input case insensitive

UPDATE: March 15, 2019
NAO added:
9. Edit use of troubleshoot multiline strings in retrieve_info and edit_book

NAO scrapped:
#4

NAO completed:
#1, 7, 9

NAO incomplete:
#2, 3, 5, 6, 8
"""
from time import sleep

# Troubleshooting instructions for user for inputting book titles
book_title_troubleshoot = """
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
edit_troubleshoot = """
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
retrieve_troubleshoot = """
--- INFORMATION RETRIEVAL TROUBLESHOOTING ---

>>> If you're having trouble retrieving information about a book, it is possible you made a typo while inputting the title of the book.

>>> Follow these instructions:
	1. Choose option 3 of the RETRIEVE INFO menu.
	2. Note down the title of the book you were trying to find. 
	3. Choose option 3 of the MAIN MENU. 
	4. Type in the incorrect title that you noted down in Step 2.
	5. Update any incorrect information. 

"""

def title_input(purpose):
	'''
	Asks user for title of a book

	purpose: str, the purpose of the function ('retrieve', 'edit', or 'new')

	Returns: str, title of book from user input, formatted in a way so that the program can use the information
	''' 

	issue_counter = 0

	while True:
		# Asks user for the title of the book
		title = input("Title of Book: ")

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
				if title not in book_list_dict:
					print('Sorry, book not found in the Book List. Please type in the title of an EXISTING book.')
					sleep(1)
					print()
					issue_counter += 1
					# Only prints the long troubleshooting instructions if this is the 3rd time
					# the user is having trouble (otherwise it gets annoying)
					if issue_counter == 3:
						# Prints out instructions on how to correctly type in a book title 
						# if book doesn't exist in book_list_dict
						for line in book_title_troubleshoot.splitlines():
							print(line)
							sleep(0.3)
						if purpose == 'retrieve':
							# Prints out retrieve troubleshoot instructions
							for line in retrieve_troubleshoot.splitlines():
								print(line)
								sleep(0.3)
						elif purpose == 'edit':
							# Prints out edit troubleshoot instructions
							for line in edit_troubleshoot.splitlines():
								print(line)
								sleep(0.3)
						first_issue = False
				# If the book does exist, exit while loop
				else:
					break

			# If block runs if user tries to create a new book that already exists in the Book List
			if purpose == 'new' and title in book_list_dict:
				print("Sorry, this book already exists in the Book List. Please type in the title of a NEW book.")
				sleep(1)
				print()
				issue_counter += 1
				# Only prints the long troubleshooting instructions if this is the first time
				# the user is having trouble (otherwise it gets annoying)
				if issue_counter == 3:
					# Prints out instructions on how to correctly type in a book title 
					# if book already exists in book_list_dict
					for line in book_title_troubleshoot.splitlines():
						print(line)
						sleep(0.3)
					first_issue = False
			# If book is a new book, exit while loop
			elif purpose == 'new' and title not in book_list_dict:
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

	Returns: rating, an int from 0-5
	'''

	while True:
		try:
			rating = int(input("Rating (out of 5 stars): "))
			# User input cannot be empty and rating must be an integer from 0-5 
			assert rating and rating <= 5 and rating >= 0
		except ValueError:
			print("Error, please enter an integer.")
		except AssertionError:
			print("Error, please enter an integer between 0 and 5.")
		else:
			return rating

def new_book():
	'''
	Takes in user input to create a new entry in the book_list_dict dictionary
		-Title (str)
		-Author (str)
		-Rating (int, 0-5)
	Then adds the information into book_list_dict

	Returns: None
	'''

	print("You have chosen option 1, to add a new book.")

	# Asks the user for the title, author, and rating.
	title = title_input("new")
	author = author_input()
	rating = rating_input()

	#Adds the title, author, and rating to the book_list_dict dictionary.
	book_list_dict[title] = [author, rating]

	#Confirmation message
	sleep(1)
	print("The book %s by %s has been added. The rating is %s out of 5 stars." % (title.upper(), author.upper(), rating))

def retrieve_info():
	'''
	Retrieves information about books in book_list_dict:
		-Rating
		-Author
		-Prints all information currently on the Book List

	Returns: None
	'''

	print("You have chosen option 2, to retrieve information about an existing book.")

	try:
		# book_list_dict must exist (have at least 1 entry)
		assert book_list_dict
	except AssertionError:
		print("Sorry, there are currently no books in the list. Please add at least 1 book before retrieving information.")
	else:
		while True:
			try:
				sleep(1)
				print("""
	--- RETRIEVE INFO MENU ---
	Would you like to:
		(1) Retrieve the RATING of a book
		(2) Retrieve the AUTHOR of a book
		(3) Retrieve ALL INFORMATION on the Book List

		(4) Return to MAIN MENU
		""")
				# Asks user about what they want to retrieve OR return to main menu.
				user_input = input("Enter 1, 2, 3, or 4: ")

				acceptable_input = ['1', '2', '3', '4']
				assert user_input in acceptable_input

			except AssertionError:
				print("Sorry, I did not understand. Please enter the number 1, 2, 3, or 4.")
			else:
				# Retrieve rating
				if user_input == '1':
					print("You have chosen option 1, to retrieve the RATING of a book.")
					# Asks user to enter the title of the book
					book = title_input("retrieve")

					# Retrieves the rating
					retrieve_rating(book)

				# Retrieve author
				elif user_input == '2':
					print("You have chosen option 2, to retrieve the AUTHOR of a book.")

					# Asks user to enter the title of the book
					book = title_input("retrieve")

					# Retrieves the author
					retrieve_author(book)

				# Retrieve all information on booklist
				elif user_input == '3':
					print("You have chosen option 3, to retrieve ALL INFORMATION on the Book List.")

					# Prints all information on the Book List
					sleep(1)
					print_all_books()

				# Return to Main Menu 
				elif user_input == '4':
					break

def retrieve_rating(book):
	'''
	book: str, title of book

	Retrieves the rating of a book

	Returns: rating, int from 0-5
	'''

	# Title is put in UPPERCASE for ease of reading.
	sleep(1)
	print("The rating of %s is: %d stars." % (book.upper(), book_list_dict[book][1]))
	return book_list_dict[book][1]

def retrieve_author(book):
	'''
	book: str, title of book

	Retrieves the author of a book

	Returns: str, author of the book
	'''

	# Title and author are put in UPPERCASE for ease of reading.
	sleep(1)
	print("The author of %s is: %s." % (book.upper(), book_list_dict[book][0].upper()))
	return book_list_dict[book][0]

def print_all_books():
	'''
	Prints all of the books in the book_list_dict and their information in a readable way:
		-Title
		-Author
		-Rating

	Returns: None
	'''

	print ("The following are all of the books in alphabetical order by title:")
	print()
	sleep(1)

	# key = str.lower to be case insenitive sorting 
	for book in sorted(book_list_dict, key = str.lower):
		sleep(0.3)
		print("%s by %s | Rating: %s out of 5 stars." % (book, book_list_dict[book][0], book_list_dict[book][1]))

def edit_title(book):
	'''
	book: str, title of book that user wants to update the title of

	Updates the title of a book

	Returns: str, new title of book
	'''

	# Variable saves original title of selected book for 
	# confirmation message and to distinguish between original and updated title
	original_title = book 

	# Author and rating of selected book saved
	author = book_list_dict[original_title][0]
	rating = book_list_dict[original_title][1]

	while True:
		try:
			# Asks user for title of the book
			new_title = input('What is the UPDATED TITLE of the book? ')

			# Checks if the title starts with the string 'The', then moves 'The' to the back of the title.
			# This is for alphabetizing purposes. 
			if new_title[:3] == "The":
				new_title = new_title[4:] + ", The"

			# New title must be a string that is not empty 
			# and not be a book that already exists (to prevent duplicates)
			assert new_title and not new_title in book_list_dict
		except AssertionError:
			# If block runs if the title_input input was empty
			if not new_title:
				print('Sorry, you did not enter a title of the book. Please try again.')
			
			# Elif block runs if the user entered a duplicate title
			elif new_title in book_list_dict:
				# Book titles capitalized for ease of reading
				print("Sorry, you are trying to change the title of %s to %s, which already exists in the Book List. You can't have duplicate titles!" % (original_title.upper(), new_title.upper()))
		else:
			break

	# Deletes key/value pairing of selected book
	del book_list_dict[original_title]

	# Creates a new key/value pairing with the updated title, but keeps the original author and rating
	book_list_dict[new_title] = [author, rating]
	
	sleep(1)
	# Confirmation message, titles uppercase for ease of reading
	print("The original title, %s, has been changed to: %s." % (original_title.upper(), new_title.upper()))

	return new_title

def edit_author(book):
	'''
	book: str, title of book that user wants to update the author of

	Updates the author of a book

	Returns: str, new author of book
	'''

	# Variable saves original author of selected book for confirmation message
	original_author = book_list_dict[book][0]

	while True:
		try:
			new_author = input('What is the UPDATED AUTHOR of the book? ')
			# New author input must not be an empty string
			assert new_author
		except AssertionError:
			print('Sorry, you did not enter an author of the book. Please try again.')
		else:
			break
	
	# Changes original author value to updated author value
	book_list_dict[book][0] = new_author

	sleep(1)
	# Confirmation message, titles uppercase for ease of reading
	print("The original author, %s, has been changed to: %s." % (original_author.upper(), new_author.upper()))

	return new_author

def edit_rating(book):
	'''
	book: str, title of book that user wants to update the rating of

	Updates the rating of a book

	Returns: int from 0-5, new rating of book
	'''

	# Variable saves original rating of selected book for confirmation message
	original_rating = book_list_dict[book][1]

	while True:
		try:
			# Asks user for updated rating
			new_rating = int(input("What is the UPDATED RATING of the book (out of 5 stars)? "))
			# User input must meet the following conditions:
			# Isn't empty, and is an integer between 0 and 5
			assert new_rating and new_rating <= 5 and new_rating >= 0
		# Raises exception if user did not enter an integer
		except ValueError:
			print('Sorry, you did not enter an integer. Please try again.')
		except AssertionError:
			# If block runs if user did not input anything
			if not new_rating:
				print('Sorry, you did not enter a rating of the book. Please try again.')
			# Elif block runs if rating is not from 0-5
			elif new_rating > 5 or new_rating < 0:
				print('Sorry, you did not enter a rating from 0-5. Please try again.')
		else:
			break

	# Changes original rating to updated rating
	book_list_dict[book][1] = new_rating

	# Confirmation message
	sleep(1)
	print("The original rating, %s, has been changed to: %s." % (original_rating, new_rating))

	return new_rating

def edit_book(): 
	'''
	Allows user to edit information on the book_list_dict that previously inputted:
		-Title
		-Author
		-Rating

	Returns: None
	'''

	print("You have chosen option 3, to edit information about an existing book.")

	edit_book_1 = True

	try:
		assert book_list_dict
	except AssertionError:
		print("Sorry, there are currently no books in the list. Please add at least 1 book before editing information.")
	else:
		# While loop for EDIT BOOK MENU 1. 
		while edit_book_1:
			print("""	--- EDIT BOOK MENU 1 --- 
		Would you like to:
		(1) CHOOSE A BOOK to edit

		(2) Return to MAIN MENU
			""")

			acceptable_input = ['1', '2']
			try:
				user_input = input("Enter 1 or 2: ")
				assert user_input in acceptable_input
			except AssertionError:
				print("Sorry, I did not understand. Please enter 1 or 2.")
			else:
				# Option 1 of EDIT BOOK MENU 1: Asks user to choose a book to edit
				if user_input == "1":
					print("You have chosen option 1. What book would you like to edit?")

					# Asks user to enter the title of the book
					book = title_input("edit")

					# Prints all information about requested book.
					sleep(1)
					print("The following is the EXISTING information in the Book List:")
					sleep(0.3)
					print("Title: %s | Author: %s | Rating (out of 5 stars): %s" % (book, book_list_dict[book][0], book_list_dict[book][1]))

					edit_book_2 = True

					# While loop for EDIT BOOK MENU 2. 
					while edit_book_2:
						sleep(1)
						print("""		--- EDIT BOOK MENU 2 --- 
			Would you like to:
				(1) Edit the TITLE
				(2) Edit the AUTHOR
				(3) Edit the RATING

				(4) DELETE the entire BOOK

				(5) Change the information about ANOTHER BOOK

				(6) Return to MAIN MENU
					""")

						acceptable_input = ['1', '2', '3', '4', '5', '6']

						try:
							user_input = input("Enter 1, 2, 3, 4, 5, or 6: ")
							assert user_input in acceptable_input
						except AssertionError:
							print("Sorry, I did not understand. Please enter 1, 2, 3, 4, 5, or 6.")
						else:
							# Option 1 of EDIT BOOK MENU 2: Edits the title of the selected book
							if user_input == "1":
								# Book variable is changed to updated title, because old title no longer exists once it is changed.
								book = edit_title(book)

							# Option 2 of EDIT BOOK MENU 2: Edits the author of the selected book
							elif user_input == "2":
								edit_author(book)
							
							# Option 3 of EDIT BOOK MENU 2: Edits the rating of the selected book
							elif user_input == "3":
								edit_rating(book)
							
							# Option 4 of EDIT BOOK MENU 2: Deletes the selected book
							elif user_input == "4":
								# Asks user for confirmation to delete
								print("""Deleting a book is PERMANENT. Continue? 
	(Y) Yes
	(N) No

	Any other character besides 'Y' will be considered 'No.'
	""")
								user_input = input("Enter Y or N: ")

								# If confirmed, deletes the book
								if user_input == "Y":
									original_title = book 
									del book_list_dict[book]
									# Confirmation message. Original title is in UPPERCASE for ease of reading
									sleep(1)
									print("The book, %s, has been deleted." % (original_title.upper()))
									# Exits out of EDIT BOOK MENU 2 
									# This is because if the user stays in EBM2, the old book (that no longer exists) is still selected
									# If user attempts to edit a book that does not exist, program will crash. 
									edit_book_2 = False
								else:
									# Confirmation message. Original title is in UPPERCASE for ease of reading
									print("Deletion of the book, %s, has been cancelled." % (original_title.upper()))

							# Option 5 of EDIT BOOK MENU 2: Change information about another book
							elif user_input == "5":
								# Exits EDIT BOOK MENU 2
								edit_book_2 = False

							# Option 6 of EDIT BOOK MENU 2: Return to MAIN MENU
							elif user_input == "6":
								# Exits EDIT BOOK MENU 2
								edit_book_2 = False

								# Exits EDIT BOOK MENU 1
								edit_book_1 = False


				# Option 2 of EDIT BOOK MENU 1: Return to MAIN MENU
				elif user_input == "2":
					# Exits EDIT BOOK MENU 1 while loop
					edit_book_1 = False

### EVERYTHING BELOW HAS NOT BEEN TRY-EXCEPT CHECKED ###

# Initial message when the program starts up
print("Welcome to the Book List!")

# This is the Book List dictionary that is created at the start of the program.
book_list_dict = {}

# Infinite while loop. Serves as the MAIN MENU.
while True:
	sleep(1)
	print("""
--- MAIN MENU --- 
Would you like to:
	(1) ADD a new book
	(2) RETRIEVE information about an existing book
	(3) EDIT information about an existing book
	(4) EXIT the program
""")
	user_wants = input("Enter 1, 2, 3, or 4: ")

	# Option 1: Adds a new book to the dictionary
	if user_wants == "1":
		new_book()

	# Option 2: Retrieves information about a book. Goes to RETRIEVE INFO MENU.
	elif user_wants == "2":
		retrieve_info()

	# Option 3: Edits information about a book. Goes to EDIT BOOK MENU 1.
	elif user_wants == "3":
		edit_book()

	# Option 4: Exits the program.
	elif user_wants == "4":
		# Asks user for confirmation about exiting the program. 
		print("""You have chosen option 4, to exit the program.
Are you sure you want to exit? All information you have inputted during this 
session will be PERMANENTLY erased. Continue?
	(Y) Yes
	(N) No
		
	Any other character besides 'Y' will be considered 'No.'
""")
		continue_exit = input("Enter Y or N: ")

		# If user confirms exit, infinite loop breaks and program stops.
		if continue_exit == "Y":
			credits = """
                                  CREDITS
Author: Rebecca Dang
Project Started: 27 Sept 2018
Project Completed: 
	Version 1: 30 Sept 2018 
	Version 2: [in progress]
Programming Language: Python 
Workspace: Sublime, Visual Studio Code
Special Thanks to: 
	Mom for the Mac
	Dad for the support
	Codecademy & edX (MITx 6.00.1x) for teaching 
If any errors occur, or if you have any inquiries, 
please contact Rebecca Dang at ph.rdang@gmail.com

"""
			for line in credits.splitlines():
				print(line)
				sleep(0.3)
			sleep(1)
			print("Thank you for using Book List! You have successfully exited the program.")
			break

	# Else block runs if user enters a string that is not 1, 2, 3, or 4.
	else:
		print("Sorry, I did not understand. Please enter the number 1, 2, 3, or 4.")