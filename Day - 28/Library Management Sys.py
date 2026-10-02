class Book:
    def __init__(self, book_id, title, author, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.available = True

    def display_books(self):
        status = "available" if self.available else "Issued"
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("status:", status)

    def issue_books(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        if not self.available:
            self.available = True
            return True
        return False


class member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def display_members(self):
        print("Member_ID:", self.member_id)
        print("Member name:", self.name)
        print("Member email:", self.email)
        print("Borrowed books")

        if len(self.borrowed_books) == 0:
            print("No books borrowed")
        else:
            for book in self.borrowed_books:
                print(book.title)

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return True
        return False


class library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print("Book Added Successfully")

    def display_book(self):
        if len(self.books) == 0:
            print("No Books Available")
            return

        for book in self.books:
            book.display_books()

    def search_book(self, keyword):
        found = False

        for book in self.books:
            if keyword.lower() in book.title.lower():
                book.display_books()
                found = True

        if not found:
            print("Book not found")

    def add_member(self, member):
        self.members.append(member)
        print("Member Added Successfully")

    def issue_book(self, book_id, member_id):
        for book in self.books:
            if book.book_id == book_id:
                for mem in self.members:
                    if mem.member_id == member_id:
                        if book.issue_books():
                            mem.borrow_book(book)
                            print("Book Issued Successfully")
                        else:
                            print("Book Already Issued")
                        return
        print("Book or Member not found")

    def return_book(self, book_id, member_id):
        for book in self.books:
            if book.book_id == book_id:
                for mem in self.members:
                    if mem.member_id == member_id:
                        if mem.return_book(book):
                            book.return_book()
                            print("Book Returned Successfully")
                        else:
                            print("Book not borrowed")
                        return
        print("Book or Member not found")