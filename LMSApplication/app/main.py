from library.library import Library

def main():
    library=Library("city Library")
    while True:
        print("\n--- Library Menu ---")
        print("1.Add Book")
        print("2.List Books")
        print("3.Search Books")
        print("4.Add Member")
        print("5.List Members")
        print("6.Borrow Books")
        print("7.Return Book")
        print("0.Exit")

        choice = input("Enter choice: ").strip


        if choice == "1":
            book_id = int(input("book id: "))
            title = input("title: ")
            author = input("author:")
            qty = int(input("quality: "))
            library.add_book(book_id,title,author,qty)

        elif choice == "2":
            for book in library.list_books():
                print(book)

        elif choice == "3":
            q = input("search title: ")
            results = library.search_books(q)

            for book in results:
                print(book)
        elif choice == "4":     
            member_id=int(input("member id: ")) 
            name=input("name: ")

            library.add_member(member_id,name)
        elif choice =="5": 
            for member in library.list_members():
                print(member)

        elif choice =="6": 
            member_id=int(input("member id: "))
            book_id=int(input("book id: "))

            if library.borrow_book(member_id,book_id):
                print("borrow successfully")
            else:
                print("borrow failed")
        elif choice == "7": 
            member_id=int(input("member id: "))
            book_id=int(input("book id: "))

            if library.return_book(member_id,book_id):
                print("returned successfully")
            else:
                print("returned failed")

        elif choice == "0":
            break

        else:
            print("invalid choice")

if __name__ == "__main__":
    main()            