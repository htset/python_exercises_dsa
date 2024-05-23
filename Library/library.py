from datetime import datetime
import os

from book import Book
from lending_event import LendingEvent

class Library:
    BooksFilename = "books.txt"
    LendingFilename = "lending_events.txt"

    def add_book(self):
        #Prompt user for book details
        title = input("Book title: ")
        author = input("Author: ")

        #Mark book as available
        book = Book(title, author, 1)

        #Append book details to books file
        with open(self.BooksFilename, 'a') as file:
            file.write(f"{book.title}|{book.author}|{book.available}\n")

        print("Book added successfully.")

    def list_books(self):
        #Check if books file exists
        if not os.path.exists(self.BooksFilename):
            print("No books entered so far")
            return

        print("Books available in the library:")
        with open(self.BooksFilename, 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                print(f"Title: {parts[0]}")
                print(f"Author: {parts[1]}")
                print(f"Available: {'True' if parts[2] == '1' else 'False'}")
                print("------------------------------")

    def lend_book(self):
        #Check if books file exists
        if not os.path.exists(self.BooksFilename):
            print("No books entered so far")
            return

        book_title = input("Enter the title of the book to lend: ")

        #Read all lines from books file
        with open(self.BooksFilename, 'r') as file:
            lines = file.readlines()

        book_found = False

        #Search for the book in the list
        for i in range(len(lines)):
            parts = lines[i].strip().split('|')
            if parts[0] == book_title and parts[2] == '1':
                lines[i] = f"{parts[0]}|{parts[1]}|0\n"
                book_found = True

                user_name = input("Enter your name: ")

                #Write lending event to lending file
                with open(self.LendingFilename, 'a') as lending_file:
                    lending_file.write(
                        f"{book_title}|{user_name}|{datetime.now()}|0\n")

                print(f"Book '{book_title}' has been lent to {user_name}.")
                break

        if not book_found:
            print(f"Book '{book_title}' not found or not available.")

        #Write updated book details back to books file
        with open(self.BooksFilename, 'w') as file:
            file.writelines(lines)

    def return_book(self):
        if not os.path.exists(self.LendingFilename):
            print("No lending events entered so far")
            return

        book_title = input("Enter the title of the book to return: ")

        #Read all lines from books file
        with open(self.BooksFilename, 'r') as file:
            books_lines = file.readlines()

        book_found = False

        #Search for the book in the list
        for i in range(len(books_lines)):
            parts = books_lines[i].strip().split('|')
            if parts[0] == book_title and parts[2] == '0':
                books_lines[i] = f"{parts[0]}|{parts[1]}|1\n"
                book_found = True

                #Read all lines from lending file
                with open(self.LendingFilename, 'r') as lending_file:
                    lending_lines = lending_file.readlines()

                #Search for the lending event
                for j in range(len(lending_lines)):
                    lending_parts = lending_lines[j].strip().split('|')
                    if lending_parts[0] == book_title and lending_parts[3] == '0':
                        lending_lines[j] = (
                            f"{lending_parts[0]}|{lending_parts[1]}|"
                            f"{lending_parts[2]}|1\n"
                        )
                        print(f"Book '{book_title}' has been returned.")
                        break

                #Write updated lending events back to lending file
                with open(self.LendingFilename, 'w') as lending_file:
                    lending_file.writelines(lending_lines)
                break

        if not book_found:
            print(f"Book '{book_title}' not found or already returned.")

        #Write updated book details back to books file
        with open(self.BooksFilename, 'w') as file:
            file.writelines(books_lines)

    def list_lending_events(self):
        if not os.path.exists(self.LendingFilename):
            print("No lending events entered so far")
            return

        print("Lending events:")
        with open(self.LendingFilename, 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                print(f"Book Title: {parts[0]}")
                print(f"User Name: {parts[1]}")
                print(f"Lending Date: {parts[2]}")
                print(f"Returned: {'True' if parts[3] == '1' else 'False'}")
                print("------------------------------")
