# This program implements an Online Book Store Management System that manages users, books, and orders.
# It includes roles such as admin, user, and guest, with various permissions and functionalities.

# The main class responsible for managing the bookstore
class OnlineBookStoreManagementSystem:
    def __init__(self):
        # Initializing the lists to store books, users, and orders, as well as the currently logged-in user
        self.books = []
        self.users = []
        self.current_user = None
        self.orders = []
        print("Welcome to the Bookiverse!")

    # Adds a new user to the system
    def add_user(self, user):
        self.users.append(user)

    # Allows users to log in by verifying their credentials
    def login(self, username, email, password):
        for user in self.users:
            # Check if the provided credentials match an existing user
            if user.username == username and user._email == email and user._Users__password == password:
                self.current_user = user
                print(f"Welcome, {user.username}! Your privilege level is '{user.privilege}'.")
                print(f"Your registered email is: {user.getEmail()}")
                print(f"Your masked password is: {user.getPassword()}")
                return
        print("Invalid credentials. Please check your username, email, or password.")

    # Displays a list of all registered users (admin-only functionality)
    def display_all_users(self):
        if self.current_user and self.current_user.privilege == "admin":
            if self.users:
                print("\n--- List of Registered Users ---")
                for user in self.users:
                    print(f"Username: {user.username}, Email: {user.getEmail()}, Privilege: {user.privilege}")
                print("--- End of List ---\n")
            else:
                print("No users are registered in the system.")

    # Allows admins to add a new book to the inventory
    def add_book(self, book):
        if self.current_user and self.current_user.privilege == "admin":
            self.books.append(book)
            print(f"Book '{book.title}' added successfully.")
            print("\nUpdated List of Books:")
            self.display_all_books()
        else:
            print("Access denied. Only admin users can add books.")

    # Allows admins to modify the details of an existing book
    def modify_book(self, title):
        if self.current_user and self.current_user.privilege == "admin":
            for book in self.books:
                if book.title.lower() == title.lower():
                    # Updating book details
                    book.price = float(input("Enter new price: "))
                    book.quantity = int(input("Enter new quantity: "))
                    print(f"\nBook '{book.title}' updated successfully!")
                    print("\nUpdated List of Books:")
                    self.display_all_books()
                    return
            print(f"Book '{title}' not found.")

    # Allows admins to delete a book from the inventory
    def delete_book(self, title):
        if self.current_user and self.current_user.privilege == "admin":
            for book in self.books:
                if book.title.lower() == title.lower():
                    self.books.remove(book)
                    print(f"Book '{book.title}' deleted successfully.")
                    print("\nUpdated List of Books:")
                    self.display_all_books()
                    return
            print(f"Book '{title}' not found.")
        else:
            print("Access denied. Only admin users can delete books.")

    # Allows admins to delete a user account
    def delete_user(self, username):
        if self.current_user and self.current_user.privilege == "admin":
            for user in self.users:
                if user.username.lower() == username.lower():
                    self.users.remove(user)
                    print(f"User '{username}' deleted successfully.")
                    print("Updated list of users:")
                    self.display_all_users()  # Display updated list of users
                    return
            print(f"User '{username}' not found.")

    # Displays all books in the inventory
    def display_all_books(self):
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("No books available.")

    # Searches for books by a specific author
    def find_books_by_author(self, author):
        results = [book for book in self.books if book.author.lower() == author.lower()]
        if results:
            for book in results:
                print(book)
        else:
            print(f"No books found by author '{author}'.")

    # Searches for books by title
    def find_books_by_title(self, title):
        results = [book for book in self.books if book.title.lower() == title.lower()]
        if results:
            for book in results:
                print(book)
        else:
            print(f"No books found with title '{title}'.")

    # Searches for books published in a specific year
    def find_books_by_year(self, year):
        results = [book for book in self.books if book.publication_year == year]
        if results:
            for book in results:
                print(book)
        else:
            print(f"No books found published in year '{year}'.")

    # Finds books within a specified price range
    def find_books_by_price_range(self, min_price, max_price):
        results = [book for book in self.books if min_price <= book.price <= max_price]
        if results:
            for book in results:
                print(book)
        else:
            print(f"No books found in the price range ${min_price} to ${max_price}.")

    # Allows users to checkout a book (reduces stock by 1)
    def checkout_book(self, title):
        if self.current_user and self.current_user.privilege in ["admin", "user"]:
            for book in self.books:
                if book.title.lower() == title.lower():
                    if book.quantity > 0:
                        book.quantity -= 1
                        print(f"Checked out: {book.title}. Remaining quantity: {book.quantity}. Book Price: {book.price}")
                        return
                    else:
                        print(f"Sorry, {book.title} is out of stock.")
                        return
            print(f"Book '{title}' not found.")

    # Allows users to place an order for a book
    def place_order(self, book_title, quantity):
        for book in self.books:
            if book.title.lower() == book_title.lower():
                if book.quantity >= quantity:
                    book.quantity -= quantity  # Reduce stock
                    order_id = len(self.orders) + 1  # Generate order ID
                    # Create an Orders object
                    order = Orders(
                        title=book.title, author=book.author, price=book.price, quantity=quantity,
                        type=book.type, publication_year=book.publication_year, genre=book.genre,
                        username=self.current_user.username, email=self.current_user._email,
                        password=self.current_user._Users__password, order_id=order_id,
                        quantity_ordered=quantity
                    )
                    self.orders.append(order)
                    print(f"Order placed successfully: {order}")
                    return
                else:
                    print("Not enough stock available for this order.")
                    return
        print("Book not found.")

    # Displays all placed orders
    def display_all_orders(self):
        if self.orders:
            for order in self.orders:
                print(order)
        else:
            print("No orders have been placed.")

    def main_menu(self):
        # Main menu for the Online Bookstore Management System
        while True:  # Keep looping until a valid choice is made
            print("Please select an option:")
            print("1. Admin Login")
            print("2. User Login")
            print("3. Guest Access")
            initial_choice = input("Enter your choice (1, 2, or 3): ")

            if initial_choice == "1":
                # Admin login flow
                username = input("Enter Admin username: ")
                email = input("Enter Admin email: ")
                password = input("Enter Admin password: ")

                # Verify admin credentials
                for user in self.users:
                    if (
                            user.username == username
                            and user._email == email
                            and user._Users__password == password  # Accessing private attribute
                            and user.privilege == "admin"
                    ):
                        print(f"Welcome Admin, {user.username}!")
                        store.current_user = user
                        break
                else:  # If no admin user matches
                    print("Invalid Admin credentials. Please try again.")
                break

            elif initial_choice == "2":
                # User login flow
                username = input("Enter User username: ")
                email = input("Enter User email: ")
                password = input("Enter User password: ")
                store.login(username, email, password)  # Call the login method for users
                break

            elif initial_choice == "3":
                # Guest access flow
                store.current_user = Users("guest", "guest@bookiverse.com", "guestpass", "guest")
                print("You are now accessing the system as a guest.")
                break  # Exit the loop for guest access

            else:
                # Handle invalid input
                print("Invalid choice. Please enter 1, 2, or 3.")

        # Menu displayed based on the user's privilege (admin, user, or guest)
        while store.current_user:
            if store.current_user.privilege == "admin":
                # Admin-specific menu options
                print("\nAdmin Menu:")
                print("1. Add a new book")
                print("2. Modify book")
                print("3. Delete book")
                print("4. Delete user account")
                print("5. Display all books")
                print("6. Find books by author")
                print("7. Find books by title")
                print("8. Find books by publication year")
                print("9. Find books by price range")
                print("10. Checkout a book")
                print("11. Place an order")
                print("12. Display all orders")
                print("13. Display all users")
                print("14. Logout")
                choice = input("Enter your choice: ")

                if choice == "1":
                    # Add a new book to the store
                    title = input("Enter book title: ")
                    author = input("Enter author: ")
                    price = float(input("Enter price: "))
                    quantity = int(input("Enter quantity: "))
                    type = input("Enter type (e.g., Hardcover, Paperback): ")
                    publication_year = int(input("Enter publication year: "))
                    genre = input("Enter genre: ")
                    store.add_book(Books(title, author, price, quantity, type, publication_year, genre))

                elif choice == "2":
                    # Modify an existing book's details
                    title = input("Enter book title to modify: ")
                    store.modify_book(title)

                elif choice == "3":
                    # Delete a book from the store
                    title = input("Enter book title to delete: ")
                    store.delete_book(title)

                elif choice == "4":
                    # Delete a user account
                    user_to_delete = input("Enter username to delete: ")
                    store.delete_user(user_to_delete)

                elif choice == "5":
                    # Display all available books
                    store.display_all_books()

                elif choice == "6":
                    # Find books by author name
                    author = input("Enter author name: ")
                    store.find_books_by_author(author)

                elif choice == "7":
                    # Find books by title
                    title = input("Enter book title: ")
                    store.find_books_by_title(title)

                elif choice == "8":
                    # Find books by publication year
                    year = int(input("Enter publication year: "))
                    store.find_books_by_year(year)

                elif choice == "9":
                    # Find books within a specified price range
                    min_price = float(input("Enter minimum price: "))
                    max_price = float(input("Enter maximum price: "))
                    store.find_books_by_price_range(min_price, max_price)

                elif choice == "10":
                    # Checkout a book
                    title = input("Enter the title of the book to checkout: ")
                    store.checkout_book(title)

                elif choice == "11":  # Place an order
                    book_title = input("Enter the title of the book to order: ")
                    quantity = int(input("Enter quantity: "))
                    store.place_order(book_title, quantity)

                elif choice == "12":  # Display all orders (admin)
                    store.display_all_orders()

                elif choice == "13":
                    # Display all user accounts
                    store.display_all_users()

                elif choice == "14":
                    # Logout
                    store.current_user = None
                    print("Logged out.")

                else:
                    # Invalid admin menu choice
                    print("Invalid choice. Please try again.")

            elif store.current_user.privilege == "user":
                # Menu for regular users
                print("\nUser Menu:")
                print("1. Display all books")
                print("2. Find books by author")
                print("3. Find books by title")
                print("4. Find books by publication year")
                print("5. Find books by price range")
                print("6. Checkout a book")
                print("7. Place an order")
                print("8. Display all orders")
                print("9. Logout")
                choice = input("Enter your choice: ")

                if choice == "1":
                    # Display all books
                    store.display_all_books()

                elif choice == "2":
                    # Find books by author
                    author = input("Enter author name: ")
                    store.find_books_by_author(author)

                elif choice == "3":
                    # Find books by title
                    title = input("Enter book title: ")
                    store.find_books_by_title(title)

                elif choice == "4":
                    # Find books by publication year
                    year = int(input("Enter publication year: "))
                    store.find_books_by_year(year)

                elif choice == "5":
                    # Find books by price range
                    min_price = float(input("Enter minimum price: "))
                    max_price = float(input("Enter maximum price: "))
                    store.find_books_by_price_range(min_price, max_price)

                elif choice == "6":
                    # Checkout a book
                    title = input("Enter the title of the book to checkout: ")
                    store.checkout_book(title)

                elif choice == "7":  # Place an order
                    book_title = input("Enter the title of the book to order: ")
                    quantity = int(input("Enter quantity: "))
                    store.place_order(book_title, quantity)

                elif choice == "8":  # Display all orders
                    store.display_all_orders()

                elif choice == "9":
                    # Logout
                    store.current_user = None
                    print("Logged out.")

                else:
                    # Invalid user menu choice
                    print("Invalid choice. Please try again.")

            elif store.current_user.privilege == "guest":
                # Menu for guest users
                print("\nGuest Menu:")
                print("1. Display all books")
                print("2. Find books by author")
                print("3. Find books by title")
                print("4. Logout")
                choice = input("Enter your choice: ")

                if choice == "1":
                    # Display all books
                    store.display_all_books()

                elif choice == "2":
                    # Find books by author
                    author = input("Enter author name: ")
                    store.find_books_by_author(author)

                elif choice == "3":
                    # Find books by title
                    title = input("Enter book title: ")
                    store.find_books_by_title(title)

                elif choice == "4":
                    # Logout
                    store.current_user = None
                    print("Logged out.")

                else:
                    # Invalid guest menu choice
                    print("Invalid choice. Please try again.")


# Class representing a Book with its details
class Books:
    def __init__(self, title, author, price, quantity, type, publication_year, genre):
        # Initializing book attributes
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity
        self.type = type
        self.publication_year = publication_year
        self.genre = genre

    def __repr__(self):
        # String representation of the Book object
        return f"Book(Title: {self.title}, Author: {self.author}, Price: ${self.price}, Quantity: {self.quantity}, Type: {self.type}, Publication Year: {self.publication_year}, Genre: {self.genre})"


# Class representing a User with their details and privileges
class Users:
    def __init__(self, username, email, password, privilege="user"):
        # Initializing user attributes
        self.username = username
        self._email = email  # Protected attribute
        self.__password = password  # Private attribute
        self.privilege = privilege  # Default privilege is "user"

    def getEmail(self):
        # Return a masked email for privacy
        return f"{self._email[:3]}{'*' * (len(self._email) - 6)}{self._email[-3:]}"

    def set_email(self, new_email):
        # Update email address
        self._email = new_email

    def set_password(self, new_password):
        # Update password
        self.__password = new_password

    def getPassword(self):
        # Return a masked password for privacy
        return 'x' * len(self.__password)

    def __repr__(self):
        # String representation of the User object
        return f"User(Username: {self.username}, Email: {self.getEmail()}, Privilege: {self.privilege})"


# Class representing an Order, combining Book and User details
class Orders(Books, Users):
    def __init__(self, title, author, price, quantity, type, publication_year, genre, username, email, password, order_id, quantity_ordered):
        # Initializing both Book and User attributes
        Books.__init__(self, title, author, price, quantity, type, publication_year, genre)
        Users.__init__(self, username, email, password)
        self.order_id = order_id  # Unique order ID
        self.quantity_ordered = quantity_ordered  # Quantity of the book ordered

    def getOrderid(self):
        # Return the order ID
        return self.order_id

    def getBook(self):
        # Return the title of the book ordered
        return self.title

    def getQuantity(self):
        # Return the quantity ordered
        return self.quantity_ordered

    def setQuantity(self, new_quantity):
        # Update the quantity ordered
        self.quantity_ordered = new_quantity

    def __repr__(self):
        # String representation of the Order object
        return f"Order(Order ID: {self.order_id}, User: {self.username}, Book: {self.title}, Quantity Ordered: {self.quantity_ordered})"


# Create an instance of the OnlineBookStoreManagementSystem class
store = OnlineBookStoreManagementSystem()

# Adding admin and user accounts
store.add_user(Users("admin1", "admin@bookiverse.com", "adminpass", "admin"))  # Admin user
store.add_user(Users("user1", "user1@bookiverse.com", "user1pass", "user"))  # Regular users
store.add_user(Users("user2", "user2@bookiverse.com", "user2pass", "user"))
store.add_user(Users("user3", "user3@bookiverse.com", "user3pass", "user"))
store.add_user(Users("user4", "user4@bookiverse.com", "user4pass", "user"))

# Adding books to the store
store.books = [
    Books("To Kill a Mockingbird", "Harper Lee", 12.99, 5, "Paperback", 1960, "Fiction"),
    Books("1984", "George Orwell", 15.99, 10, "Hardcover", 1949, "Dystopian"),
    Books("Pride and Prejudice", "Jane Austen", 9.99, 7, "Paperback", 1813, "Romance"),
    Books("The Great Gatsby", "F. Scott Fitzgerald", 14.99, 8, "Hardcover", 1925, "Classic"),
    Books("The Catcher in the Rye", "J.D. Salinger", 10.99, 6, "Paperback", 1951, "Classic")
]

# Start the main menu of the application
store.main_menu()
