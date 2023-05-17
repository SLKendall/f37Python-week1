my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def book_parser(book_dictionary):

    book_string = f"The book is {book_dictionary['title']}. The author is {book_dictionary['author']}. It was published in {book_dictionary['year']}. The rating is {book_dictionary['rating']} and the pagecount is {book_dictionary['pages']}."

    return book_string

print(book_parser(my_book))




# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def get_book_title(book_dictionary):
    
    book_title = book_dictionary["title"]
    
    return book_title

def get_book_author(book_dictionary):
    
    book_author = book_dictionary["author"]
    
    return book_author

def get_book_year(book_dictionary):
    
    book_year = book_dictionary["year"]
    
    return book_year

def get_book_rating(book_dictionary):
    
    book_rating = book_dictionary["rating"]
    
    return book_rating

def get_book_pages(book_dictionary):
    
    book_pages = book_dictionary["pages"]
    
    return book_pages

print(get_book_title(my_book))

print(get_book_author(my_book))

print(get_book_year(my_book))

print(get_book_rating(my_book))

print(get_book_pages(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def book_parser_list(dictionary_list):
    for book_dictionary in dictionary_list:
        print(book_parser(book_dictionary))

def get_set_of_authors(dictionary_list):
    author_list = []

    for book_dictionary in dictionary_list:
        author_list.append(book_dictionary["author"])

    return author_list

def get_total_pages(dictionary_list):
    total_pages = 0

    for book_dictionary in dictionary_list:
        total_pages += book_dictionary["pages"]

    return total_pages
