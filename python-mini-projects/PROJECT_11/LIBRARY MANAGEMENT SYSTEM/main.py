#LIBRARY MANAGEMENT SYSTEM
class library :
    def __init__(self,lib_name):
        self.name = lib_name
        self.books = []
        print(f"welcome to {self.name} ! The system is now online")

    def show_av_books(self) :
        if len(self.books) == 0 :
            print("The library is currently empty ! No books are available.")
        else :
            print(f"Books available in {self.name} is -")
            for book in self.books :
                print(f"- {book}")

    def add_book(self,book_name) :
        self.books.append(book_name)
        print(f"successfully! {book_name} is added to the self")

    def issue_book(self,book_name) :
        if book_name in self.books :
            self.books.remove(book_name)
            print(f" Success: '{book_name}' has been issued to you. Happy reading!")
        else :
            print(f"❌ Error: Sorry, '{book_name}' is not available right now.")

    def return_book(self,book_name) :
        self.books.append(book_name)
        print(f"Thank you ! For returning {book_name}")

# --- RUNNING THE APPLICATION ---

# 1. Instantiate the object
my_library = library("City Central Library")

# 2. Pre-load a few books so the library isn't empty when starting
my_library.add_book("Python Crash Course")
my_library.add_book("Harry Potter")
my_library.add_book("The Hobbit")

# 3. The Infinite Loop for the User Interface
while True:
    print("\n=============================")
    print("      LIBRARY MENU")
    print("=============================")
    print("1. Show Available Books")
    print("2. Add a Book")
    print("3. Issue a Book")
    print("4. Return a Book")
    print("5. Close System")
    
    choice = input("\nSelect an option (1-5): ").strip()

    if choice == "1":
        my_library.show_av_books()
    elif choice == "2":
        new_title = input("Enter the title of the book to add: ").strip()
        if new_title: # Makes sure the user didn't just press enter blankly
            my_library.add_book(new_title)
        else:
            print("❌ Title cannot be empty!")

    elif choice == "3":
        issue_title = input("Enter the title of the book to borrow: ").strip()
        my_library.issue_book(issue_title)

    elif choice == "4":
        return_title = input("Enter the title of the book to return: ").strip()
        my_library.return_book(return_title)

    elif choice == "5":
        print(f"\nShutting down system. Thank you for visiting {my_library.name}! 👋")
        break # Breaks the while loop to end execution

    else:
        print("❌ Invalid entry! Please type a number from 1 to 5.")