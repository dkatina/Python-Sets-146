# **Objective:**

# Create a Python program to manage a library's book catalog. The program should 
#allow the removal of books from the catalog and ensure the catalog remains accurate and up-to-date.

# **Problem Statement:**

# A library needs to keep its book catalog updated by removing outdated or damaged 
#books. Your task is to develop a Python script that facilitates the addition of unique books 
#from the library's catalog, which is represented as a set.

# **Instructions:**

# 1. Initialize a set with a predefined list of books. Each book is identified by its title.
# 2. Implement a function to add a book from the catalog by its title.
# 3. Provide options for the user to add a book or display the current catalog.
# 4. Ensure that we only add unique books 
# 5. Use try-except blocks to handle any unexpected errors or invalid inputs from the user.



def book_keeper():
    catalog = {"The Party by Robyn Harding", "Smoke in Mirrors by Niel Gaiman", "Fifty Shades of Grey by E.L. James"}

    while True:
        action = input('''
    1.) Add Book
    2.) View Catalog
    3.) Quit
    > ''').lower()    
        if action == '1' or action == 'add book':
            add_books(catalog)
        elif action == '2' or action == 'view catalog':
            view_catalog(catalog)
        elif action == '3' or action == 'quit':
            print('Have a nice Day')
            break
        else:
            print('Invalid Action Please try again')



def add_books(catalog):

    while True:
        book_title = input('What is the title of the book you wish to add? ').title().strip(' !@#$$^&*()')
        author = input(f'Who wrote {book_title}? ').title().strip(' !@#$$^&*()')

        catalog.add(f'{book_title} by {author}')
        
        another = input("Do you wish to add another book? 'y' or 'n'? ").lower()
        if another != 'y' or another != 'yes':
            break


def view_catalog(catalog):
    print('In no particular order...')
    print('Here are the books in your catalog:')
    print('------------------------------------')
    for idx, book in enumerate(catalog):
        print(f'{idx + 1}.) {book}')


book_keeper()