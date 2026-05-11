class dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        self.tricks = []
    
    def learn_trick(self,trick):
        self.tricks.append(trick)
    
    def __str__(self):
        return f"{self.name},{self.breed}"
    
    def __len__(self):
        return len(self.tricks)
d1 = dog("Cupcake","Pug")
d1.learn_trick("sit")
d1.learn_trick("High Five")
print(len(d1))

class book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.borrowed = False
    
    def __str__(self):
        status = "borrowed" if self.borrowed else "Available"
        return f"{self.title} by {self.author} [{status}]"
    
    def __len__(self):
        return f"{self.pages}"

class library:
    def __init__(self,name):
        self.name = name
        self.books = []
    
    def add_books(self,book):
        self.books.append(book)
        print(f"Added : {book.title}")

    def find_book(self,title):
        for book in self.books:
            if book.title.lower()==title.lower():
                return book
        return None 

b1 = book("Harry Potter","Jk Rowling",500)
b2 = book("RatBurger","David Walliams",300)
b3 = book("Wings of fire","Tui Sutherland",250)
lib = library("Aarush's Library")
lib.add_books(b1)
lib.add_books(b2)
lib.add_books(b3)
print(lib.find_book("RatBurger"))


    
