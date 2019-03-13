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
"""
from time import sleep

# Troubleshooting instructions for user if book query doesn't exist
book_does_not_exist = """Sorry, this book does not exist in the Book List. Please check the following:
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

def new_title(purpose):
	'''
	Deals with the user inputting the title of a book

	purpose: string, the purpose of the function ('retrieve', 'update', or 'new')

	Returns title of book from user input, formatted in a way so that the program can use the information
	''' 

	# Variable used for continuous check of data entered. 
	enter_title = True	
	# Checks if the new_title function is being used for retrieval or update. If so, it doesn't need to check if the title already occurs.
	if purpose == "retrieve" or purpose == "update":
		while enter_title == True:
			# Asks user for the title of the book
			title = input("Title of Book: ")
			# Checks if user has inputted anything
			if len(title) == 0:
				print("Sorry, you did not enter a title of the book.")
			else:
				# Exits enter title while loop
				enter_title = False

				# Checks if the title starts with the string 'The', then moves 'The' to the back of the title.
				# This is for alphabetizing purposes. 
				if title[:3] == "The":
					title = title[4:] + ", The"

				return title

	# Checks if the new_title function is being used to add a new book. If so, it DOES need to check if the title already occurs. 
	elif purpose == "new":
		while enter_title == True:
			# Asks user for the title of the book
			title = input("Title of Book: ")
			# Checks if user has inputted anything
			if len(title) == 0:
				print("Sorry, you did not enter a title of the book.")
			# Checks if user is inputting a title that already exists
			elif title in book_list_dict:
				print("Sorry, you are entering a new book that already exists in the Book List. Please type in the title of a NEW book.")
			else:
				# Exits enter title while loop
				enter_title = False

				# Checks if the title starts with the string 'The', then moves 'The' to the back of the title.
				# This is for alphabetizing purposes. 
				if title[:3] == "The":
					title = title[4:] + ", The"

				return title

def new_author():
	# This function allows for a new author to be added.

	# Variable used for continuous check of data entered. 
	enter_author = True
	while enter_author == True:
		# Asks user for the author of the book
		author = input("Author: ")
		# Checks if user has inputted anything
		if len(author) == 0:
			print("Sorry, you did not enter an author of the book.")
		else:
			enter_author = False
			return author
 
def new_rating():
	'''
	Lets new rating of book to be added
	Returns rating, an int from 0-5
	'''

	while True:
		try:
			rating = int(input("Rating (out of 5 stars): "))
			assert type(rating) == int and rating <= 5 and rating >= 0
		except ValueError:
			print("Error, please enter an integer.")
		except AssertionError:
			print("Error, please enter an integer between 0 and 5.")
		else:
			return rating

def new_book():
	# This function takes in user input and organizes it, as described in objectives 1 and 2.

	print("You have chosen option 1, to add a new book.")

	# Asks the user for the title, author, and rating.
	title = new_title("new")
	author = new_author()
	rating = new_rating()

	#Adds the title, author, and rating to the book_list_dict dictionary.
	book_list_dict[title] = [author, rating]

	#Confirmation message
	sleep(1)
	print("The book %s by %s has been added. The rating is %s out of 5 stars." % (title.upper(), author.upper(), rating))

def retrieve_info():
	# This function retrieves values as described in objective 3, and prints it as described in objective 4.
	
	# Troubleshooting instructions; printed whenever necessary
	retrieve_troubleshoot = """
>>> If the issue continues, follow these instructions:
	1. Choose option 3 of the RETRIEVE INFO menu.
	2. Note down the title of the book you were trying to find. It is possible you made a typo while inputting the title of the book.
	3. Choose option 3 of the MAIN MENU. 
	4. Type in the incorrect title that you noted down in Step 2.
	5. Update any incorrect information. 
"""

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
					book = new_title("retrieve")

					# Checks if the title requested is in the dictionary.
					if book in book_list_dict:
						# Retrieves the rating
						retrieve_rating(book)

					# Else block runs if title is not in the dictionary.
					else:
						# Prints out instructions on how to correctly type in a book title
						# Also prints some instructions for troubleshooting
						sleep(1)
						print(book_does_not_exist)
						sleep(1)
						print(retrieve_troubleshoot)

				# Retrieve author
				elif user_input == '2':
					print("You have chosen option 2, to retrieve the AUTHOR of a book.")

					# Asks user to enter the title of the book
					book = new_title("retrieve")

					# Checks if the title requested is in the dictionary.
					if book in book_list_dict:
						# Retrieves the rating
						retrieve_author(book)

					# Else block runs if title is not in the dictionary.
					else:
						# Prints out instructions on how to correctly type in a book title
						# Also prints some instructions for troubleshooting
						sleep(1)
						print(book_does_not_exist)
						sleep(1)
						print(retrieve_troubleshoot)

				# Retrieve all information on booklist
				elif user_input == '3':
					print("You have chosen option 3, to retrieve ALL INFORMATION on the Book List.")

					# Prints all information on the Book List
					sleep(1)
					print_all_books()

				# Return to Main Menu (also option 4)
				# Exits out of retrieve_info input while loop
				break 

### EVERYTHING BELOW HAS NOT BEEN TRY-EXCEPT CHECKED ###
def retrieve_rating(book):
	# This function retrieves the rating of a book.
	# Title is put in UPPERCASE for ease of reading.
	sleep(1)
	print("The rating of %s is: %d stars." % (book.upper(), book_list_dict[book][1]))

def retrieve_author(book):
	# This function retrieves the author of a book.
	# Title and author are put in UPPERCASE for ease of reading.
	sleep(1)
	print("The author of %s is: %s." % (book.upper(), book_list_dict[book][0].upper()))

def print_all_books():
	# This function prints all of the books in the list book_list. 

	print ("The following are all of the books in alphabetical order by title:")
	sleep(1)

	# key = str.lower to be case insenitive sorting 
	for book in sorted(book_list_dict, key = str.lower):
		sleep(0.3)
		print("%s by %s | Rating: %s out of 5 stars." % (book, book_list_dict[book][0], book_list_dict[book][1]))

def update_title(book):
	# This function updates the title of a book.

	# Variable saves original title of selected book for 
	# confirmation message and to distinguish between original and updated title
	original_title = book 

	# Author and rating of selected book saved
	author = book_list_dict[original_title][0]
	rating = book_list_dict[original_title][1]

	# Variable used for continuous check of data entered. 
	enter_title = True	
	while enter_title == True:
		# Asks user for the title of the book
		new_title = input("What is the UPDATED TITLE of the book? ")
		# Checks if user has inputted anything
		if len(new_title) == 0:
			print("Sorry, you did not enter a title of the book.")
		# Checks if user has inputted a title that already exists 
		elif new_title in book_list_dict:
			print("Sorry, you are trying to change the title of %s to %s, which already exists in the Book List. You can't have duplicate titles!" % (original_title, new_title))
			# Returns to EDIT BOOK MENU 2
			enter_title = False
			return None 
		else:
			# Exits enter title while loop
			enter_title = False

			# Checks if the title starts with the string 'The', then moves 'The' to the back of the title.
			# This is for alphabetizing purposes. 
			if new_title[:3] == "The":
				new_title = new_title[4:] + ", The"

	# Deletes key/value pairing of selected book
	del book_list_dict[original_title]

	# Creates a new key/value pairing with the updated title, but keeps the original author and rating
	book_list_dict[new_title] = [author, rating]
	
	# Confirmation message
	sleep(1)
	print("The original title, %s, has been changed to: %s." % (original_title, new_title))

	return new_title

def update_author(book):
	# This function updates the author of a book.

	# Variable saves original author of selected book for confirmation message
	original_author = book_list_dict[book][0]

	# Variable used for continuous check of data entered. 
	enter_author = True
	while enter_author == True:
		# Asks user for updated author
		new_author = input("What is the UPDATED AUTHOR of the book? ")
		# Checks if user has inputted anything
		if len(new_author) == 0:
			print("Sorry, you did not enter an author of the book.")
		else:
			enter_author = False
			
	# Changes original author value to updated author value
	book_list_dict[book][0] = new_author

	# Confirmation message
	sleep(1)
	print("The original author, %s, has been changed to: %s." % (original_author, new_author))

def update_rating(book):
	# Variable saves original rating of selected book for confirmation message
	original_rating = book_list_dict[book][1]

	# Variable used for continuous check of data entered. 
	enter_rating = True
	while enter_rating == True:
		# Asks user for updated rating
		new_rating = input("What is the UPDATED RATING of the book (out of 5 stars)? ")
		# Checks if user has inputted anything
		if len(new_rating) == 0:
			print("Sorry, you did not enter a rating of the book.")
			# Checks if the user has inputted an integer.
		if new_rating.isdigit() == False:
			print("Please enter an integer between 0 and 5.")
		# Checks if user has inputted a string that is completely digits.
		# Thus, any negative values or floats will not be accepted.
		if new_rating.isdigit() == True:
			# Checks if user has inputted a rating that is greater than 5.
			if int(new_rating) > 5:
				print("Sorry, you entered a rating greater than 5. Please enter an integer between 0 and 5.")
			# Checks if user has inputted an integer between 0 and 5. 
			if int(new_rating) <= 5:
				# Exits rating while loop
				enter_rating = False

	# Changes original rating to updated rating
	book_list_dict[book][1] = new_rating

	# Confirmation message
	sleep(1)
	print("The original rating, %s, has been changed to: %s." % (original_rating, new_rating))

def edit_book(): 
	# This function allows the user to edit information that was previously inputted.

	# Troubleshooting instructions; printed whenever necessary
	edit_troubleshoot = """
>>> If the issue continues, follow these instructions:
	1. Choose option 2 of the EDIT BOOK MENU 1.
	2. Choose option 2 of the MAIN MENU.
	3. Choose option 3 of the RETRIEVE INFO menu.
	4. Note down the title of the book you were trying to find. It is possible you made a typo while inputting the title of the book.
	5. Choose option 3 of the MAIN MENU. 
	6. Type in the incorrect title that you noted down in Step 3.
	7. Update any incorrect information. 
"""	

	# Variable used to stay/switch between menus.
	edit_book = True 

	print("You have chosen option 3, to edit information about an existing book.")

	# Checks if the book_list_dict is empty; if it is, it prompts the user to add a book before proceeding.	
	if len(book_list_dict) == 0:
		# Prevents going into EDIT BOOK MENU 1
		edit_book = False
		print("Sorry, there are currently no books in the list. Please add at least 1 book before editing information.")

	# While loop, condition checks if user should still be in the EDIT BOOK MENU 1. 
	while edit_book == True:
		print("""--- EDIT BOOK MENU 1 --- 
	Would you like to:
	(1) CHOOSE A BOOK to edit

	(2) Return to MAIN MENU
		""")

		user_wants_edit_1 = input("Enter 1 or 2: ")

		# Option 1: Asks user to choose a book to edit
		if user_wants_edit_1 == "1":

			print("You have chosen option 1. What book would you like to edit?")

			# Asks user to enter the title of the book
			book = new_title("update")

			# Checks if the title requested is in the dictionary
			if book in book_list_dict:
				# Exits out of EDIT BOOK MENU 1 
				edit_book = False

				# Enters EDIT BOOK MENU 2
				edit_book_2 = True

				# Prints all information about requested book.
				sleep(1)
				print("The following is the EXISTING information in the Book List:")
				sleep(0.3)
				print("Title: %s | Author: %s | Rating (out of 5 stars): %s" % (book, book_list_dict[book][0], book_list_dict[book][1]))

				# While loop, condition checks if user should still be in the EDIT BOOK MENU 2. 
				while edit_book_2 == True:
					sleep(1)
					print("""--- EDIT BOOK MENU 2 --- 
			Would you like to:
				(1) Edit the TITLE
				(2) Edit the AUTHOR
				(3) Edit the RATING

				(4) DELETE an entire BOOK

				(5) Change the information about ANOTHER BOOK

				(6) Return to MAIN MENU
					""")

					user_wants_edit_2 = input("Enter 1, 2, 3, 4, 5, or 6: ")

					# Option 1: Edits the title of the selected book
					if user_wants_edit_2 == "1":
						# Book variable is changed to updated title, because old title no longer exists once it is changed.
						book = update_title(book)

					# Option 2: Edits the author of the selected book
					elif user_wants_edit_2 == "2":
						update_author(book)
					
					# Option 3: Edits the rating of the selected book
					elif user_wants_edit_2 == "3":
						update_rating(book)
					
					# Option 4: Deletes the selected book
					elif user_wants_edit_2 == "4":
						# Asks user for confirmation to delete
						print("""Deleting a book is PERMANENT. Continue? 
	(Y) Yes
	(N) No

	Any other character besides 'Y' will be considered 'No.'
	""")
						continue_delete_book = input("Enter Y or N: ")

						# If confirmed, deletes the book
						if continue_delete_book == "Y":
							original_title = book 
							del book_list_dict[book]
							# Confirmation message. Original title is in UPPERCASE for ease of reading
							sleep(1)
							print("The book, " + original_title.upper() + ", has been deleted.")
							# Exits out of EDIT BOOK MENU 2 
							# This is because if the user stays in EBM2, the old book (that no longer exists) is still selected
							# If user attempts to edit a book that does not exist, program will crash. 
							edit_book_2 = False

							# Returns to EDIT BOOK MENU 1
							edit_book = True 

					# Option 5: Return to EDIT BOOK MENU 1 to choose another book to edit
					elif user_wants_edit_2 == "5":
						# Exits EDIT BOOK MENU 2
						edit_book_2 = False

						# Returns to EDIT BOOK MENU 1
						edit_book = True 

					# Option 6: Return to MAIN MENU
					elif user_wants_edit_2 == "6":
						# Exits EDIT BOOK MENU 2
						edit_book_2 = False

						# Exits EDIT BOOK MENU 1
						edit_book = False

					# Else block runs if user entered in a string that is not 1, 2, 3, 4, 5, or 6.
					else:
						print("Sorry, I did not understand. Please enter 1, 2, 3, 4, 5, or 6.")
			# Else block runs if title is not in the dictionary
			else:
				# Prints out instructions on how to correctly type in a book title
				# Also prints some instructions for troubleshooting
				sleep(1)
				print(book_does_not_exist)
				sleep(1)
				print(edit_troubleshoot)

		# Option 2: Return to MAIN MENU
		elif user_wants_edit_1 == "2":
			# Exits EDIT BOOK MENU 1
			edit_book = False

		# Else block runs if user entered in a string that is not 1 or 2.
		else:
			print("Sorry, I did not understand. Please enter 1 or 2.")

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
			print("""
                                  CREDITS
Author: Rebecca Dang
Project Started: September 27, 2018
Project Completed: September 30, 2018 
Programming Language: Python 
Workspace: Sublime 
Special Thanks to: Mom for the Mac, Dad for the support, and Codecademy for teaching 
If any errors occur, or if you have any inquiries, 
please contact Rebecca Dang at ph.rdang@gmail.com

""")
			sleep(1)
			print("Thank you for using Book List! You have successfully exited the program.")
			break

	# Else block runs if user enters a string that is not 1, 2, 3, or 4.
	else:
		print("Sorry, I did not understand. Please enter the number 1, 2, 3, or 4.")