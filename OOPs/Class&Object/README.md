# Object-Oriented Programming (OOPS) in Python

## What is OOPS?

OOPS (Object-Oriented Programming System) is a programming paradigm based on the concept of **objects**, which contain:

* **Data** → Attributes
* **Behavior** → Methods

OOPS helps in writing **reusable, scalable, and organized code**.

---

## Programming Approaches Comparison

### 1. Imperative Approach

```python
a = 12
b = 12
print(a + b)
```

* Simple and straightforward
* Not reusable
* Requires new variables for every new operation

---

### 2. Functional Approach

```python
def addition(a, b):
    return a + b

print(addition(12, 12))
print(addition(45, 45))
```

* Reusable
* Cleaner than imperative
* Still limited for complex real-world modeling

---

### 3. Object-Oriented Approach

```python
class Addition:
    def __init__(self, a, b):
        print(a + b)

obj = Addition(12, 12)
```

* Models real-world entities
* Code is modular and reusable
* Foundation for large applications

---

## Core OOPS Concepts

* Class
* Object
* Constructor
* Encapsulation
* Inheritance
* Polymorphism

(This section focuses on **Class, Object, and Constructor**.)

---

## Classes in Python

### What is a Class?

A **class** is a blueprint or template for creating objects.

Example:

```python
class Car:
    brand = "Toyota"
```

* The class defines **what an object will have**
* The object is the **actual implementation**

---

### Attributes and Methods

* **Attributes** → Variables inside a class
* **Methods** → Functions inside a class

Example:

```python
class Animal:
    species = "Dog"   # Attribute

    def make_sound(self):   # Method
        print("Bark!")
```

---

## Accessing Attributes and Methods

```python
class Animal:
    type = "Cat"

    def sound(self):
        print("Meow!")

print(Animal().type)   # Access attribute
Animal().sound()       # Call method
```

* A class is initialized when an object is created
* Attributes and methods are accessed using objects

---

## Objects in Python

### What is an Object?

An **object** is an instance of a class.
It has **all the properties and behavior of the class**.

### Real-World Analogy

* Class → Bag Factory (Blueprint)
* Object → Reebok Bag, Campus Bag
* Attributes → Material, Zips, Pockets

---

## Object Syntax

```python
class Fruit:
    name = "Apple"

f = Fruit()       # Object creation
print(f.name)    # Access attribute
```

---




