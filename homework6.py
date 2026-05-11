class Bookshelf:
    def __init__(self, owner):
        self.owner = owner
        self.books = []

    def add_book(self, title):
        self.books.append(title)
    
    def __str__(self):
        return f"{self.owner},{self.books}"

    def __len__(self):
        return len(self.books)

shelf = Bookshelf("Aryan")
shelf.add_book("Billianare boy")
shelf.add_book("Cursed child")
shelf.add_book("Atomic Habits")
print(shelf)        
print(len(shelf)) 


class Playlist:
    def __init__(self, name):
        self.name  = name
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __str__(self):
        return f"Playlist: {self.name} | {len(self.songs)} songs"

    def __len__(self):
        return len(self.songs)

p = Playlist("Chill Mix")
p.add("Song A")
p.add("Song B")
print(p)
print(len(p))
p.add("Song C")
print(p)
print(f"The playlist has {len(p)} songs")


class Team:
    def __init__(self, name):
        self.name    = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def __str__(self):             
        return f"{self.name}: {len(self.players)} players"

    def __len__(self):             
        return len(self.name)

team = Team("India")
team.add_player("Rohit")
team.add_player("Virat")
print(team)
print(len(team))


class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
    def __str__(self):
        return f"{self.name}: {self.mark}"

class Classroom:
    def __init__(self):
        self.students = []
    def enrol(self, student):
        self.students.append(student)
    def top_student(self):
        return max(self.students, key=lambda s: s.mark)
    def class_average(self):
        total = sum(s.mark for s in self.students)
        return round(total / len(self.students), 1)

room = Classroom()
room.enrol(Student("Aryan", 88))
room.enrol(Student("Priya", 95))
room.enrol(Student("Rahul", 72))
print(room.top_student())
print(room.class_average())


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ₹{self.price}"


class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def cheapest(self):
        return min(self.products, key=lambda p: p.price)

    def total_value(self):
        return sum(p.price for p in self.products)

    def __len__(self):
        return len(self.products)

shop = Shop()

p1 = Product("Pen", 10)
p2 = Product("Book", 50)
p3 = Product("Bag", 500)

shop.add_product(p1)
shop.add_product(p2)
shop.add_product(p3)

print("Cheapest:", shop.cheapest())
print("Total value:", shop.total_value())
print("Number of products:", len(shop))


class car:
    def __init__(self,brand,colour,price):
        self.brand = brand
        self.colour = colour
        self.price = price
    
    def __str__(self):
        return f"{self.brand},{self.colour},{self.price}"
    
    def __len__(self):
        return len(self.brand)
    
class showroom:
    def __init__(self,name):
        self.name = name
        self.cars = []
    
    def add_car(self,car):
        self.cars.append(car)
    

    def show_cars(self):
        print(f"Cars in {self.name}:")
        for car in self.cars:
            print(car)   
    
    def cheapest_car(self):
        return min(self.cars,key = lambda c:c.price)
    
    def total_money(self):
        return sum(c.price for c in self.cars)
    
    def __len__(self):
        return len(self.cars)

showroom = showroom("Luxury Cars")
c1 = car("Toyota", "Fortuner", 4000000)
c2 = car("Honda", "City", 1500000)
c3 = car("BMW", "X5", 8000000)

showroom.add_car(c1)
showroom.add_car(c2)
showroom.add_car(c3)

showroom.show_cars()

print("Cheapest:", showroom.cheapest_car())
print("Total value:", showroom.total_money())
print("Number of cars:", len(showroom))


