# This is a deliberately poorly implemented main script for a Library Management System.

from book import Book
from user import User
from check import Check
from logger import Logger

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. List Users")
    print("5. Display default book attributes")
    print("6. Change default book attributes")
    print("7. Display default user attributes")
    print("8. Change default user attributes")
    print("9. Edit Book details")
    print("10. Edit User details")
    print("11. CheckOut a book")
    print("12. CheckIn a book")
    print("13. Delete all book details")
    print("14. Delete all user details")
    print("15. Delete a specific book details")
    print("16. Delete a specific user details")
    print("17. Search by specific details in books")
    print("18. Search by specific details in user")
    print("19. Display the log")
    print("E. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    book = Book('bookData')
    user = User('userData')
    check = Check('bookData','userData')
    logger = Logger('logData')
    while True:
        choice = main_menu()
        if choice == '1':
            book.addBookDetails()
        elif choice == '2':
            book.getAll()
        elif choice == '3':
            user.addUserDetails()
        elif choice == '4':
            user.getAll()
        elif choice == '5':
            book.getDefaultAttributes()
        elif choice == '6':
            book.changeDefaultAttributes()
        elif choice == '7':
            user.getDefaultAttributes()
        elif choice == '8':
            user.changeDefaultAttributes()
        elif choice == '9':
            book.editData()
        elif choice == '10':
            user.editData()
        elif choice == '11':
            bookId = input("Enter the book id : ")
            userId = input("Enter the user id : ")
            check.checkOut(bookId, userId)
        elif choice == '12':
            bookId = input("Enter the book id : ")
            userId = input("Enter the user id : ")
            check.checkIn(bookId, userId)
        elif choice == '13':
            book.deleteAll()
        elif choice == '14':
            user.deleteAll()
        elif choice == '15':
            book.delete()
        elif choice == '16':
            user.delete()
        elif choice == '17':
            book.get()
        elif choice == '18':
            user.get()
        elif choice == '19':
            logger.getAllActions()
        elif choice == 'E':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
