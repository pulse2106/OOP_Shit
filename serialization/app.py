import pickle
import os
from datetime import datetime
from libs.lib_system import LibrarySystem
from libs.book import Book
from libs.member import Member

DATA_FILE = "library_data.pkl"


def save_system(system):
    with open(DATA_FILE, "wb") as f:
        pickle.dump(system, f)
    print("💾 Data saved (application shutdown)")


def load_system():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as f:
            system = pickle.load(f)
        print("📂 Data loaded (application startup)")
        return system
    else:
        print("🆕 No existing data, creating new system")
        return LibrarySystem()


def reset():
    os.remove(DATA_FILE)


def main():
    system = load_system()

    while True:
        print("\n1. Add Book")
        print("2. Add Member")
        print("3. Lend Book")
        print("4. Show Data")
        print("5. Exit")
        print("10. Clear Data")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            system.add_book(Book(book_id, title))

        elif choice == "2":
            member_id = input("Member ID: ")
            name = input("Name: ")
            system.add_member(Member(member_id, name))

        elif choice == "3":
            book_id = input("Book ID: ")
            member_id = input("Member ID: ")
            system.lend_book(book_id, member_id)

        elif choice == "4":
            system.show_data()

        elif choice == "5":
            save_system(system)
            print("👋 Exiting application...")
            break

        elif choice == "10":
            print("Clearing the Library System !!!!!!")
            reset()
            print("Clearing the Library System ........ Done")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
