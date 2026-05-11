class animal:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def __str__(self):
        return f"{self.name} {self.age}"

class dog(animal):
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed

d = dog("Bruno",12,"labrador")
d.sleep()
d.eat()
print(d)

