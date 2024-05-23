import sys
from library import Library

def main():
    lib = Library()
    while True:
        print("\n1. Add a book\n2. List all books\n3. Lend a book"
              "\n4. Return a book\n5. List lending events\n0. Exit")
        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == 1:
            lib.add_book()
        elif choice == 2:
            lib.list_books()
        elif choice == 3:
            lib.lend_book()
        elif choice == 4:
            lib.return_book()
        elif choice == 5:
            lib.list_lending_events()
        elif choice == 0:
            print("Exiting.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
