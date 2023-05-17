### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
# with open("library.txt", "w") as f:
#     f.write("On Lighthouses, Christina MacSweeney, 2020, 4, 174\n")

library = "library.txt"

def create_new_book(library):
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

    with open(library, "a") as f:
        f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")


### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
def view_user_books(library):

    with open(library, "r") as f:
        file = f.readlines()

        for line in file:
            title, author, year, rating, pages = line.split(", ")

            print(f"Title: {title}. Author: {author}. Year published: {year}, Rating: {rating}, Pagecount: {pages}")

# view_user_books()

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!


def book_list_dictionary(library):
    books_list = []

    with open(library, "r") as f:
        file = f.readlines()
        
        for line in file:
            title, author, year, rating, pages = line.split(", ")
            books_list.append({
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            })
    return books_list

def get_book_printed(book):
    print(f"Title: {book['title']}, \nAuthor: {book['author']}, \nYear: {book['year']}, \nRating: {book['rating']}, \nPages: {book['pages']}")


def print_books_by_rating(library):
    
    list = book_list_dictionary(library)
    
    list = sorted(list, key = lambda x: float(x["rating"]), reverse = True)

    for book in list:
        get_book_printed(book)

def print_total_page_count(library):

    total_page_count = 0

    with open(library, "r") as f:
        file = f.readlines()

        for line in file:
            title, author, year, rating, pages = line.split(", ")
            page_count = int(pages)
            total_page_count += page_count
            
    print(f"{total_page_count} is the total pagecount of all the books in your library")


def main_menu(library):
     active = True

     while active:
          
        selection = input("Select 1 to add a book. \nSelect 2 to view your books. \nSelect 3 to view total page count of your books. \nSelect 4 to view your books organized by rating. \nSelect 5 to exit. \nInput selection: ")

        if selection == "1":
            create_new_book(library)
        elif selection == "2":
            view_user_books(library)
        elif selection == "3":
            print_total_page_count(library)
        elif selection == "4":
            print_books_by_rating(library)
        elif selection == "5":
            print("\nGoodbye")
            active = False
        else:
            print("\nPlease input a valid number to select an option.\n")

if __name__ == "__main__":
    main_menu("library.txt")