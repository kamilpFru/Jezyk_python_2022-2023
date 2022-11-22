# podpunkt A) 
# zdefiniować w ramach klasy A funkcję foo(self, x), metodę klasy class_foo, metodę statyczną static_foo, 
# tak, żeby kod poniżej drukował treści jak w komentarzach

class A(object):
    def foo(self, x):
        print(f'wykonanie foo({self}, {x})')

    @classmethod
    def class_foo(cls, x):
        print(f'class_foo({cls}, {x}')

    @staticmethod
    def static_foo(x):
        pass

a = A()
a.foo(123) # wykonanie foo(<__main__.A object at 0x0000023A680D1F10>, 123)
A.foo(a,123) # ditto
a.class_foo(123) # class_foo(<class '__main__.A'>, 123)
A.class_foo(123) # ditto
a.static_foo(123) # wykonanie static_foo(123)
A.static_foo(123) # ditto

# podpunkt B)
# zdefiniować dowolną klasę bazową dziedzicząca z ABC i posiadającą metodę abstrakcyjną
# po czym zdefiniować ze dwie klasy potomne z odpowiednimi definicjami, zademonstrować w działaniu
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, sound):
        self.sound = sound

    def speak(self):
        return self.sound

class Cat(Animal):
    def __init__(self, sound):
        self.sound = sound

    def speak(self):
        return self.sound

dog = Dog('hau')
print(dog.speak())

cat = Cat('miau')
print(cat.speak())

# podpunkt C)
# zdefiniować dowolną klasę oraz atrybut klasy tak, że stanie się on atrybutem czytanym poprzez 
# dekorator @property, a ustawianym za pomocą @nazwa.setter, pokazać w działaniu

class Employee:
    def __init__(self):
        print('Dodano pracownika')
        self._salary = 0
    
    @property
    def salary(self):
        print('Pensja pracownika: ', end='')
        return self._salary

    @salary.setter
    def salary(self, salary):
        print('Dodano kwote pensji pracownika:', salary)
        self._salary = salary

employee1 = Employee()
print(employee1.salary)
employee1.salary = 3500
print(employee1.salary)