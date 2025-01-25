class Book:
    def __init__(self,title,author,year):

        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def show_info(self):
        if self. available == True:
            print(f'Available! The Book Is {self.title} The Author Is {self.author}')
        else :
            print("Not Found")

    def borrow(self):
        if self.available == True:
            
            self.available = False
            print(f"You Have Borrowed {self.title}")
        else:
            print("not available")

    def return_book(self):

        self.available = True
        print(f'{self.title} is now available')


class Fiction(Book):

    def __init__(self,title,author,year,gener):
        super().__init__(title,author,year)
        self.gener = gener

    def show_info(self):
        print(f'The Book Gener Is {self.gener}')
        
        
        
class Science(Book):
    def __init__(self,title,author,year,field):
        super().__init__(title,author,year)
        self.field = field

    def show_info(self):
        print(f'The Book Gener Is {self.field}')

class Library:

    def __init__(self):

        self.books=[]

    def add_book(self,book):

        self.books.append(book)
        print(f"The {book.title} is added succsfully!")

    def book_info(self):
            if len(self.books)==0:
            print("The No Books To Show")
        else:
            for i in self.books:
                print(i.show_info)


l1 = Library()

book1= Fiction("introduction","fatma",1999,"fantazy")
book2 = Science("intro","fatma",2025,"bio")

l1.add_book(book1)
l1.add_book(book2)

l1.book_info()













        
        
        





        



              
            
