class Library:
    def __init__(self):
        """Initialize the library with an empty book catalog."""
        self.books = {}

    def add_book(self, title, copies=1):
        """
        Add a book to the library or increase its copies if it already exists.

        :param title: The title of the book
        :param copies: Number of copies to add (default is 1)
        """
        if title in self.books:
            self.books[title] += copies
        else:
            self.books[title] = copies
        print(f"'{title}' has been added with {copies} copies.")

    def borrow_book(self, title):
        """
        Borrow a book from the library.

        :param title: The title of the book to borrow
        """
        if title in self.books and self.books[title] > 0:
            self.books[title] -= 1
            print(f"You have borrowed '{title}'.")
            if self.books[title] == 0:
                print(f"'{title}' is now out of stock.")
        else:
            print(f"Sorry, '{title}' is not available.")

    def return_book(self, title):
        """
        Return a borrowed book to the library.

        :param title: The title of the book to return
        """
        if title in self.books:
            self.books[title] += 1
            print(f"Thank you for returning '{title}'.")
        else:
            print(f"'{title}' is not recognized in our catalog. Adding it as a new book.")
            self.add_book(title)

    def display_books(self):
        """Display the current book catalog."""
        if not self.books:
            print("The library catalog is empty.")
        else:
            print("\nLibrary Catalog:")
            for title, copies in self.books.items():
                print(f" - {title}: {copies} copies")


# Main Program
if __name__ == "__main__":
    library = Library()
    print("Welcome to the Library Management System!")

    while True:
        print("\nMenu:")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Display Books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter the book title: ")
            copies = int(input("Enter the number of copies: "))
            library.add_book(title, copies)
        elif choice == "2":
            title = input("Enter the book title to borrow: ")
            library.borrow_book(title)
        elif choice == "3":
            title = input("Enter the book title to return: ")
            library.return_book(title)
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
