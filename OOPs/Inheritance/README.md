# Inheritance in Python (OOPS)

## What is Inheritance?

In general terms, inheritance means receiving property or possession from a predecessor.

In **Python OOPS**, inheritance works **between classes**, not people.

👉 **Inheritance allows a child class to inherit attributes and methods from a parent class.**

---

## Why Use Inheritance?

Inheritance provides:

* **Code reusability**
* **Organized structure**
* **Easy maintenance and extension**
* **Reduced redundancy**

---

## Basic Syntax of Inheritance

```python
class Parent:
    def speak(self):
        print("I can speak!")

class Child(Parent):
    pass
```

* The child class automatically gets access to all attributes and methods of the parent class.

---

## Accessing Parent Properties

```python
obj = Child()
obj.speak()
```

---

## Constructor in Inheritance

### Case 1: Parent Has Constructor, Child Does Not

* The parent’s constructor is automatically called.

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def display(self):
        print(self.name)
```

---

### Case 2: Child Has Its Own Constructor

* Parent constructor is **NOT called automatically**
* Use `super()` to call the parent constructor

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        print(f"My name is {self.name} and I am {self.age} years old")
```

* `super()` targets the parent class
* Initializes parent attributes inside child class

---

## Method Overriding

* If child class defines a method with the **same name** as parent
* Child method **overrides** the parent method

```python
class Animal:
    def show(self):
        print("I am an animal")

class Human(Animal):
    def show(self):
        print("I am a human")
```

---

## Example: Inheritance with Constructor and Override

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Animal name is {self.name}")

class Human(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show(self):
        print(f"Human age is {self.age}")

person1 = Human("Yash", 20)
person1.show()

animal1 = Animal("Lion")
animal1.show()
```

---

## Types of Inheritance

### 1. Single Inheritance

* One parent → one child

```python
class Parent:
    pass

class Child(Parent):
    pass
```

---

### 2. Multiple Inheritance

* Multiple parents → one child
* Python follows **MRO (Method Resolution Order)**

```python
class Father:
    def skills(self):
        print("Coding")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    def show(self):
        print("I have multiple skills")
```

⚠ If both parents have the same method, Python uses **left-to-right order**.

---

### 3. Multilevel Inheritance

* Grandparent → Parent → Child

```python
class Grandparent:
    def heritage(self):
        print("Heritage from Grandparent")

class Parent(Grandparent):
    pass

class Child(Parent):
    pass
```

---

## Real-World Factory Example

```python
class Factory:
    def __init__(self, material, zip):
        self.material = material
        self.zip = zip

class FactoryMumbai(Factory):
    def __init__(self, material, zip, color):
        super().__init__(material, zip)
        self.color = color

class FactoryPune(FactoryMumbai):
    def __init__(self, material, zip, color, pockets):
        super().__init__(material, zip, color)
        self.pockets = pockets
```

---

## Multiple Inheritance & MRO Example

```python
class Animal:
    def __init__(self, name):
        pass

class Human:
    def __init__(self, name, age):
        pass

class Robots(Animal, Human):
    name3 = "Yash"
```

* Python checks classes **from left to right**
* This order is called **MRO (Method Resolution Order)**

---

## Important Notes

* Parent constructor is **not automatic** if child defines its own `__init__`
* Use `super()` to access parent constructor
* Child class can override parent methods
* Python supports **multiple inheritance** (unlike Java)

---

## Key Takeaways

* Inheritance promotes **code reuse**
* `super()` connects child to parent
* Method overriding allows customization
* MRO decides which parent method is called

---
