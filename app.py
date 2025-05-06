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




