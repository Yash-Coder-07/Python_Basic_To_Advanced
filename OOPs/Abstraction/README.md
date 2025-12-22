# Abstraction in Python (OOPS)

## What is Abstraction?

Abstraction is an OOPS concept used to **simplify complex systems** by:

* Showing only **essential features**
* Hiding **unnecessary implementation details**
* Defining a **common interface** for different subclasses

⚠️ Python does not support abstraction directly like Java or C++,
but it **achieves abstraction using the `abc` module**.

---

## Abstract Classes and Methods

### Abstract Class

* An **abstract class** is a class that **cannot be instantiated**
* It may contain **one or more abstract methods**
* Used as a blueprint for other classes

### Abstract Method

* A method that is **declared but not implemented**
* Subclasses **must implement** all abstract methods

---

## Using `abc` Module

Python provides the `abc` (Abstract Base Class) module.

```python
from abc import ABC, abstractmethod
```

---

## Basic Example of Abstraction

```python
from abc import ABC, abstractmethod

class Animal(ABC):        # Abstract class
    @abstractmethod
    def make_sound(self):
        pass
```

### Implementing Abstract Methods in Child Classes

```python
class Dog(Animal):
    def make_sound(self):
        print("Dog says Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Cat says Meow!")
```

---

## Reference Example (From Your Code)

### Abstract Class

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass
```

---

### Child Class (Incomplete Implementation ❌)

```python
class Square(Shape):
    def __init__(self, side):
        self.side = side
```

❌ This will raise an error if you try to create an object,
because `perimeter()` and `area()` are not implemented.

---

### Child Class (Complete Implementation ✅)

```python
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        print("I created a perimeter")

    def area(self):
        print("I created area")
```

### Creating Object

```python
obj = Circle(6)
obj.perimeter()
obj.area()
```

---

## Important Rules of Abstraction

* Abstract classes **cannot be instantiated**
* All abstract methods **must be implemented** in child classes
* If even one abstract method is missing → object creation fails
* Abstraction enforces **method consistency**

---

## Why Use Abstraction?

* Ensures **standard structure**
* Improves **code readability**
* Reduces **implementation complexity**
* Helps in **large-scale application design**

---

## Comparison with Encapsulation

| Concept       | Purpose                               |
| ------------- | ------------------------------------- |
| Encapsulation | Hides data using access control       |
| Abstraction   | Hides implementation using interfaces |

---

## Key Takeaways

* Abstraction focuses on **what to do**, not **how to do**
* Achieved in Python using `ABC` and `@abstractmethod`
* Forces subclasses to follow a contract
* Essential for scalable OOPS design
