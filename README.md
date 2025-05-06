# Python Object-Oriented Programming (OOP) Assignments

This repository contains solutions to 21 Python OOP assignments that cover various OOP concepts like `self`, `cls`, access modifiers, static methods, decorators, inheritance, exception handling, and more.

## Assignments

### 1. **Using `self`**
- Created a `Student` class with attributes `name` and `marks`.
- Used `self` to initialize these values via a constructor and added a method `display()` to print student details.

### 2. **Using `cls`**
- Created a `Counter` class that keeps track of how many objects have been created using a class variable.
- Used a class method to manage and display the count.

### 3. **Public Variables and Methods**
- Created a `Car` class with a public variable `brand` and a public method `start()`.
- Instantiated the class and accessed both from outside the class.

### 4. **Class Variables and Class Methods**
- Created a `Bank` class with a class variable `bank_name` and a class method `change_bank_name()` to change the bank name, affecting all instances.

### 5. **Static Variables and Static Methods**
- Created a `MathUtils` class with a static method `add(a, b)` to return the sum.

### 6. **Constructors and Destructors**
- Created a `Logger` class that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

### 7. **Access Modifiers: Public, Private, and Protected**
- Created an `Employee` class with public, protected, and private variables and tried accessing all three from an object.

### 8. **The `super()` Function**
- Created a `Person` class and inherited a `Teacher` class, using `super()` to call the base class constructor.

### 9. **Abstract Classes and Methods**
- Created an abstract `Shape` class with an abstract method `area()`, and inherited a `Rectangle` class that implements the `area()` method.

### 10. **Instance Methods**
- Created a `Dog` class with instance variables `name` and `breed` and an instance method `bark()` that prints a message with the dog's name.

### 11. **Class Methods**
- Created a `Book` class with a class variable `total_books` and a class method `increment_book_count()` to increase the count when a new book is added.

### 12. **Static Methods**
- Created a `TemperatureConverter` class with a static method `celsius_to_fahrenheit(c)` that returns the Fahrenheit value.

### 13. **Composition**
- Created a `Car` class that uses composition by passing an `Engine` object to it during initialization. Accessed a method of the `Engine` class via the `Car` class.

### 14. **Aggregation**
- Created a `Department` class and an `Employee` class that uses aggregation by having a `Department` object store a reference to an `Employee` object.

### 15. **Method Resolution Order (MRO) and Diamond Inheritance**
- Created four classes `A`, `B`, `C`, and `D` to demonstrate MRO, with `D` inheriting from both `B` and `C` and calling a method from class `B` due to MRO.

### 16. **Function Decorators**
- Wrote a decorator function `log_function_call` that prints "Function is being called" before a function executes. Applied it to the function `say_hello()`.

### 17. **Class Decorators**
- Created a class decorator `add_greeting` that modifies a class to add a `greet()` method returning "Hello from Decorator!". Applied it to a class `Person`.

### 18. **Property Decorators: @property, @setter, and @deleter**
- Created a `Product` class with a private attribute `_price` and used `@property`, `@setter`, and `@deleter` to manage the price.

### 19. **`callable()` and `__call__()`**
- Created a `Multiplier` class with a `__call__()` method to allow instances to be called like a function. Demonstrated this with the `callable()` function.

### 20. **Creating a Custom Exception**
- Created a custom exception `InvalidAgeError` and wrote a function `check_age(age)` that raises this exception if the age is less than 18.

### 21. **Making a Custom Class Iterable**
- Created a `Countdown` class that takes a start number and implemented `__iter__()` and `__next__()` to make the object iterable in a `for` loop, counting down to 0.

