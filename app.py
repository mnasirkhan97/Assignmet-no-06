#  1. Using self
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage:
student1 = Student("Ali", 85)
student1.display()


#  2. Using cls
class Counter:
    count = 0  # Class variable to keep track of object count

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")

# Example usage:
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.show_count()


# 3. Public Variables and Methods
class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):  # Public method
        print(f"{self.brand} car is starting...")

# Example usage:
car1 = Car("Toyota")
print(car1.brand)  # Accessing public variable
car1.start()       # Calling public method


#  4. Class Variables and Class Methods
class Bank:
    bank_name = "ABC Bank"  # Class variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show_bank(self):
        print(f"Bank Name: {Bank.bank_name}")

# Example usage:
b1 = Bank()
b2 = Bank()

b1.show_bank()
b2.show_bank()

Bank.change_bank_name("XYZ Bank")

b1.show_bank()
b2.show_bank()


# 5. Static Variables and Static Methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Example usage:
result = MathUtils.add(5, 7)
print(f"Sum: {result}")

# 6. Constructors and Destructors
class Logger:
    def __init__(self):
        print("Logger object has been created.")

    def __del__(self):
        print("Logger object is being destroyed.")

# Example usage:
log = Logger()
del log  # Manually destroying to show the destructor message immediately


# 7. Access Modifiers: Public, Protected, and Private
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            # Public
        self._salary = salary       # Protected
        self.__ssn = ssn            # Private

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

# Example usage:
emp = Employee("John", 50000, "123-45-6789")

# Accessing a public variable
print("Public:", emp.name)

# Accessing protected variable (allowed but not recommended)
print("Protected:", emp._salary)

# Accessing a private variable directly will raise AttributeError
try:
    print("Private:", emp.__ssn)
except AttributeError:
    print("Private: Cannot access directly")

# Accessing private using name mangling (not recommended)
print("Private (via name mangling):", emp._Employee__ssn)


# 8. The super() Function
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call base class constructor
        self.subject = subject

    def display(self):
        print(f"Name: {self.name}, Subject: {self.subject}")

# Example usage:
teacher = Teacher("Sara", "Mathematics")
teacher.display()


# 9. Abstract Classes and Methods (using the abc module)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example usage:
rect = Rectangle(5, 4)
print("Area of rectangle:", rect.area())


# 10. Instance Methods
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

# Example usage:
dog1 = Dog("Buddy", "Labrador")
dog1.bark()

# 11. Class Methods
class Book:
    total_books = 0  # Class variable

    def __init__(self, title):
        self.title = title
        Book.total_books += 1  # Increment the total count when a new book is added

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def show_book_count(cls):
        print(f"Total books: {cls.total_books}")

# Example usage:
book1 = Book("Python Programming")
book2 = Book("Data Science with Python")

Book.show_book_count()  # Display total books

Book.increment_book_count()  # Increment the count
Book.show_book_count()


# 12. Static Methods
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example usage:
celsius = 25
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is {fahrenheit}°F")


# 13. Composition
class Engine:
    def start_engine(self):
        print("Engine is starting...")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine

    def start(self):
        print("Car is starting...")
        self.engine.start_engine()  # Access Engine's method via Car

# Example usage:
engine = Engine()
car = Car(engine)
car.start()


# 14. Aggregation
class Department:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department  # Aggregation: Employee has a Department

    def show_details(self):
        print(f"Employee: {self.name}, Department: {self.department.name}")

# Example usage:
dept = Department("Engineering")
emp = Employee("Alice", dept)
emp.show_details()


# 15. Method Resolution Order (MRO) and Diamond Inheritance
class A:
    def show(self):
        print("A's show method")

class B(A):
    def show(self):
        print("B's show method")

class C(A):
    def show(self):
        print("C's show method")

class D(B, C):
    pass

# Example usage:
d = D()



# 16. Function Decorators
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

# Example usage:
say_hello()


# 17. Class Decorators
def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"  # Adding a greet method to the class
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage:
person = Person("John")
print(person.greet())  # Output: Hello from Decorator!

d.show()  # This will call the method from class B due to MRO


# 18. Property Decorators: @property, @setter, and @deleter 
class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        return self._price  # Getter for price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value  # Setter for price

    @price.deleter
    def price(self):
        print("Deleting price")
        del self._price  # Deleter for price

# Example usage:
product = Product(100)
print(product.price)  # Accessing the price

product.price = 150  # Using setter
print(product.price)

del product.price  # Using deleter



