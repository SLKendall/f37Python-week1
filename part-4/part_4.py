### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

# title = input("Input the title of your book:")
# author = input("Input the author of your book")
# year = input ("Input the year the book was published")
# rating = input("Input your rating (up to 5) of your book")
# pages = input("Input your book's pagecount")

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# title = input("Input the title of your book:")
# author = input("Input the author of your book")
# year = int(input ("Input the year the book was published"))
# rating = float(input("Input your rating (up to 5) of your book"))
# pages = int(input("Input your book's pagecount"))


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

# title = input("Input the title of your book:")
# author = input("Input the author of your book:")

# try:
#     year = int(input("Input the year the book was published:"))
# except:
#     year = int(input("Please input a number:"))

# try:    
#     rating = float(input("Input the rating you would assign to your book:"))
# except:
#     rating = float(input("Please input a number:"))

# try:   
#     pages = int(input("Input your book's pagecount:"))
# except:
#     pages = int(input("Please input a number:"))

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

# def main_menu(books_source):
        
#         selection = input("Select 1 to add a book. \nSelect 2 to view your books. \nSelect 3 to exit")

#         if selection == "1":
#              books_source.append(create_new_book())
#         elif selection == "2":
#              print("\nGoodbye")
#              active = False
#         else:
#              print("\nPlease input a valid number to select an option.")

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

current_books = [
    {
        "title": "On Lighthouses",
        "author": "Christina MacSweeney",
        "year": 2020,
        "rating": 4,
        "pages": 174
    },
    {
        "title": "Infinite Jest",
        "author": "David Foster Wallace",
        "year": 1996,
        "rating": 4.5,
        "pages": 1079
    },
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "year": 1998,
        "rating": 3.9,
        "pages": 182
    }
]

def create_new_book():
    title = input("Input the title of your book:")
    author = input("Input the author of your book:")
    try:
        year = int(input("Input the year the book was published:"))
    except:
        year = int(input("Please input a number:"))
    try:    
        rating = float(input("Input the rating you would assign to your book:"))
    except:
        rating = float(input("Please input a number:"))
    try:   
        pages = int(input("Input your book's pagecount:"))
    except:
        pages = int(input("Please input a number:"))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    
    return book_dictionary

def print_all_books(list_of_books):
     
     print("Here are your books:")

     for book in list_of_books:
          title = book["title"]
          author = book["author"]
          year = book["year"]
          rating = book["rating"]
          pages = book["pages"]

          print(f"Title: {title} \nAuthor: {author} \nYear: {year} \nRating: {rating} \nPages: {pages}")

def main_menu(books_source):
     active = True

     while active:
          
        selection = input("Select 1 to add a book. \nSelect 2 to view your books. \nSelect 3 to view total page count of your books. \nSelect 4 to exit. \nInput selection: ")

        if selection == "1":
            books_source.append(create_new_book())
        elif selection == "2":
            print_all_books(books_source)
        elif selection == "3":
            print(f"\nYour total page count is {sum([x['pages'] for x in books_source])} pages.\n")
        elif selection == "4":
            print("\nGoodbye")
            active = False
        else:
            print("\nPlease input a valid number to select an option.\n")

main_menu(current_books)