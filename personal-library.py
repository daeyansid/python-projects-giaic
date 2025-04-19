# Personal Library Manager
# A command-line application to manage a personal book collection

import json
import os

class LibraryManager:
    def __init__(self):
        self.library = []
        self.filename = "library.txt"
        self.load_library()
        
    def add_book(self):
        """Add a new book to the library"""
        print("\nAdd a new book:")
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        
        # Validate publication year
        while True:
            try:
                year = int(input("Enter the publication year: "))
                break
            except ValueError:
                print("Please enter a valid year (numeric value).")
        
        genre = input("Enter the genre: ")
        
        # Validate read status
        while True:
            read_status = input("Have you read this book? (yes/no): ").lower()
            if read_status in ['yes', 'no']:
                break
            print("Please enter 'yes' or 'no'.")
        
        book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read_status == "yes"
        }
        
        self.library.append(book)
        print("Book added successfully!")
    
    def remove_book(self):
        """Remove a book from the library"""
        if not self.library:
            print("Your library is empty.")
            return
            
        title = input("Enter the title of the book to remove: ")
        found = False
        
        for i, book in enumerate(self.library):
            if book["title"].lower() == title.lower():
                del self.library[i]
                print("Book removed successfully!")
                found = True
                break
                
        if not found:
            print(f"No book found with title '{title}'.")
    
    def search_book(self):
        """Search for a book by title or author"""
        if not self.library:
            print("Your library is empty.")
            return
            
        print("Search by:")
        print("1. Title")
        print("2. Author")
        
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice in [1, 2]:
                    break
                print("Please enter 1 or 2.")
            except ValueError:
                print("Please enter a number.")
        
        search_key = "title" if choice == 1 else "author"
        search_value = input(f"Enter the {search_key}: ")
        
        matches = []
        for book in self.library:
            if search_value.lower() in book[search_key].lower():
                matches.append(book)
        
        if matches:
            print("\nMatching Books:")
            for i, book in enumerate(matches, 1):
                read_status = "Read" if book["read"] else "Unread"
                print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
        else:
            print(f"No books found matching that {search_key}.")
    
    def display_all_books(self):
        """Display all books in the library"""
        if not self.library:
            print("Your library is empty.")
            return
            
        print("\nYour Library:")
        for i, book in enumerate(self.library, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    
    def display_statistics(self):
        """Display statistics about the library"""
        total_books = len(self.library)
        
        if total_books == 0:
            print("Your library is empty.")
            return
            
        read_books = sum(1 for book in self.library if book["read"])
        percent_read = (read_books / total_books) * 100
        
        print(f"\nTotal books: {total_books}")
        print(f"Percentage read: {percent_read:.1f}%")
    
    def save_library(self):
        """Save the library to a file"""
        try:
            with open(self.filename, "w") as file:
                json.dump(self.library, file)
            print(f"Library saved to {self.filename}.")
        except Exception as e:
            print(f"Error saving library: {e}")
    
    def load_library(self):
        """Load the library from a file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    self.library = json.load(file)
                print(f"Library loaded from {self.filename}.")
            except Exception as e:
                print(f"Error loading library: {e}")
                self.library = []
        else:
            print("No saved library found. Starting with an empty library.")
            self.library = []
    
    def display_menu(self):
        """Display the main menu"""
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
    
    def run(self):
        """Run the main program loop"""
        while True:
            self.display_menu()
            
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a number between 1 and 6.")
                continue
            
            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.remove_book()
            elif choice == 3:
                self.search_book()
            elif choice == 4:
                self.display_all_books()
            elif choice == 5:
                self.display_statistics()
            elif choice == 6:
                self.save_library()
                print("Library saved to file. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    library_manager = LibraryManager()
    library_manager.run()