#Question 2: Library Book Reservation System
#Design a Python program for a Library Book Reservation System. Create a function 
#reserve_book(book_title, student_status) that allows students to reserve a book. If the book is available 
#and the student is a regular student, reserve the book; if the student is a VIP student, provide instant 
#reservation. Handle cases where the book is not available.
books = ["book1","book2","Book3","book4","book5"]
print(books)
bn = input("Enter book name from aboves : ")
n = input("Enter your name : ")
status = input("Enter your status : Vip or avg : ").lower()

attendence = float(input("Enter your attendence : 0-100 : "))

def reserve_book(book_title,student_status):
    global books
    if bn not in books:
        print("not found")
    elif attendence < 50:
        print("cant assign book")
    elif status == "vip":
       print("here is your book")
    else:
        print("Wai 10 mins to find the book ")

reserve_book(bn,status)
    
    
