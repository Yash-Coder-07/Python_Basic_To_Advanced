# Attributes and Methods in Python (OOPS)

## Types of Attributes

### 1. Class Attribute

* A **class attribute** is a variable defined inside a class but outside any method.
* It is **shared by all objects** of the class.

```python
class Car:
    wheels = 4   # Class attribute
```

---

### 2. Instance Attribute

* An **instance attribute** is created using `self` inside the constructor.
* It is **unique to each object**.

```python
class Car:
    wheels = 4   # Class attribute

    def __init__(self, color):
        self.color = color   # Instance attribute
```

---

## Types of Methods

### 1. Instance Method

* Works with the **instance (object)** of the class.
* Can access and modify **instance attributes**.
* Uses `self` as the first parameter.

```python
class MyClass:
    def instance_method(self):
        print("This is an instance method")
```

---

### 2. Class Method

* Works with the **class itself**, not with individual objects.
* Uses the `@classmethod` decorator.
* Takes `cls` as the first parameter.
* Commonly used to access or modify class-level data.

```python
class MyClass:
    @classmethod
    def class_method(cls):
        print("This is a class method")
```

---

### 3. Static Method

* Does **not** access class or instance directly.
* Uses the `@staticmethod` decorator.
* Acts like a normal function placed inside a class.

```python
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method")
```

---

## Complete Example: Attributes and Methods

```python
class Animal:
    name = "Lion"    # Class attribute

    def __init__(self, age):
        self.age = age   # Instance attribute

    def show(self):      # Instance method
        print(f"Your animal age is {self.age}")

    @classmethod
    def hello(cls):     # Class method
        print("Hello, how are you?")

    @staticmethod
    def static():       # Static method
        print("I am a static method")
```

### Creating an Object

```python
obj = Animal(12)

obj.show()          # Instance method
Animal.hello()      # Class method
Animal.static()     # Static method
```

---

## Key Differences Summary

| Feature              | Instance Method | Class Method   | Static Method   |
| -------------------- | --------------- | -------------- | --------------- |
| Decorator            | None            | `@classmethod` | `@staticmethod` |
| First Parameter      | `self`          | `cls`          | None            |
| Access Instance Data | Yes             | No             | No              |
| Access Class Data    | Yes             | Yes            | No              |

---

## Key Takeaways

* **Class attributes** are shared across all objects.
* **Instance attributes** are unique per object.
* **Instance methods** work with object data.
* **Class methods** work with class-level data.
* **Static methods** are utility functions inside a class.

---

