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

