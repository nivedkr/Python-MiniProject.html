def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)
    print(f"Added: '{title}'")

def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print(f"Book ID {book_id} borrowed successfully.")
    else:
        print(f"Cannot borrow Book ID {book_id}: Either doesn't exist or already borrowed.")

def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book ID {book_id} returned.")
    else:
        print(f"Book ID {book_id} was not borrowed.")

def register_member(members, member_id):
    members.add(member_id)
    print(f"Registered member: {member_id}")

def show_available(catalog, borrowed_books):
    print("\n--- Available Books ---")
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            print(f"ID {book_id}: {details[0]} by {details[1]} ({details[2]})")
    print("-----------------------\n")

def main():
    catalog = {}
    borrowed_books = []
    members = set()

    add_book(catalog, 101, "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    add_book(catalog, 102, "1984", "George Orwell", 1949)
    add_book(catalog, 103, "To Kill a Mockingbird", "Harper Lee", 1960)
    add_book(catalog, 104, "Brave New World", "Aldous Huxley", 1932)

    register_member(members, "M001")
    register_member(members, "M002")
    register_member(members, "M001") 
    register_member(members, "M003")

    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)

    return_book(borrowed_books, 101)

    show_available(catalog, borrowed_books)

if __name__ == "__main__":
    main()
