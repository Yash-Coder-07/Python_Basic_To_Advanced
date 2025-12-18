# Polymorphism in Python (OOPS)

## What is Polymorphism?

Polymorphism is a core concept of Object-Oriented Programming (OOPS).
The word *polymorphism* means **“many forms”**.

In programming, polymorphism allows the **same method name or interface** to behave **differently depending on the object or context**.

---

## Types of Polymorphism in Python

Python achieves polymorphism mainly in **two ways**:

### 1. Method Overriding

* Occurs when a **child class defines a method with the same name** as in the parent class.
* The child class method **overrides** the parent method.
* Method selection happens at **runtime**.

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

obj = Dog()
obj.sound()
```

---

### Important Note on Method Overloading

* Python **does not support method overloading** in the traditional sense.
* If multiple methods with the same name are defined, the **latest definition overrides previous ones**.

```python
def show():
    print("How are you")

def show():
    print("You are best")

show()
```

---

## Method Overriding Example

```python
class Animal:
    def show(self):
        print("Hello I am Yash")

class Human(Animal):
    def show(self):
        print("How are you..?")

obj = Human()
obj.show()
```

---

## 2. Duck Typing

Python follows the philosophy:

> *“If it walks like a duck and quacks like a duck, it must be a duck.”*

* Python does not care about the object’s class.
* It only cares whether the object has the required method.

```python
class Duck:
    def talk(self):
        print("Quack!")

class Human:
    def talk(self):
        print("Hello!")

def speak(obj):
    obj.talk()

speak(Duck())
speak(Human())
```

---

## Polymorphism Without Inheritance

Polymorphism can exist **without inheritance** if multiple classes have methods with the same name.

```python
class Animal:
    def show(self):
        print("Hello I am showing")

class Human:
    def show(self):
        print("Hello I am also showing")

obj1 = Animal()
obj2 = Human()

obj1.show()
obj2.show()
```

---

## Key Takeaways

* Polymorphism means **one interface, many implementations**
* Python supports polymorphism via:

  * Method overriding
  * Duck typing
* Method overloading is **not supported**
* Behavior is decided **at runtime**