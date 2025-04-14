import json
import os

'''
This is the file in which data of library will be stored
'''
LIBRARY_FILE = "library.txt"

# Load library from file
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Format a single book for display
def format_book(book, index=None):
    status = "Read" if book["read"] else "Unread"
    book_info = f'{book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {status}'
    return f"{index + 1}. {book_info}" if index is not None else book_info

# Add a book
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = int(input("Enter the publication year: ").strip())
    genre = input("Enter the genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = read_input == "yes"
    library.append({
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    })
    print("Book added successfully!")

# Remove a book by title
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip().lower()
    for book in library:
        if book["title"].lower() == title:
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

# Search for a book
def search_books(library):
    print("Search by: \n1. Title \n2. Author")
    choice = input("Enter your choice: ").strip()
    keyword = input("Enter the search term: ").strip().lower()
    matches = []

    if choice == "1":
        matches = [book for book in library if keyword in book["title"].lower()]
    elif choice == "2":
        matches = [book for book in library if keyword in book["author"].lower()]
    else:
        print("Invalid choice.")
        return

    if matches:
        print("Matching Books:")
        for i, book in enumerate(matches):
            print(format_book(book, i))
    else:
        print("No matching books found.")

# Display all books
def display_all_books(library):
    if not library:
        print("Your library is empty.")
    else:
        print("Your Library:")
        for i, book in enumerate(library):
            print(format_book(book, i))

# Display statistics
def display_statistics(library):
    total = len(library)
    read_count = sum(1 for book in library if book["read"])
    percentage = (read_count / total * 100) if total else 0
    print(f"Total books: {total}")
    print(f"Percentage read: {percentage:.1f}%")

# Show menu
def show_menu():
    print("\nWelcome to your Personal Library Manager!\n")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit\n\n")

# Main loop
def main():
    library = load_library()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
