class animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")
    
class dog(animal):
    def __init__(self,name):
        self.name = name 
    
    def speak(self):
        print(f"{self.name} barks")

a = dog("Bruno")
a.speak()

from abc import ABC,abstractmethod
class animal (ABC):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @abstractmethod
    def speak(self):
        pass
    
    @abstractmethod
    def move(self):
        pass
    
    def eat(self):
        print(f"{self.name} is eating")

    def __str__(self):
        return f"{self.name} (age{self.age})"
        
   # a = animal("Generic",5)

class fish(animal):
    def move(self):
        print(f"{self.name} swims.")

#f = fish("Nemo",2) #TypeError: Can't instantiate abstract class fish without an implementation for abstract method 'speak'

class dog(animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age) #Since we did not iniate the animal class we iniate it in child class
        self.breed = breed
    
    def speak(self):
        print(f"{self.name} barks!")
    
    def move(self):
        print(f"{self.name} runs on 4 legs")
    
    def __str__(self):
        return f"{self.name} the {self.breed} (age{self.age})"
    
d = dog("Bruno",5,"Pug")
d.speak()
d.move()
