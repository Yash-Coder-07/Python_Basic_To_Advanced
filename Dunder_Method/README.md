# Dunder (Magic) Methods in Python

## What are Dunder Methods?

Dunder methods (short for **double underscore methods**) are special methods in Python that:

* Start and end with **double underscores**
  (e.g. `__init__`, `__str__`, `__add__`)
* Are **automatically called** when certain operations are performed
* Allow you to **customize the behavior of your class**

They make user-defined objects behave like **built-in data types** (int, str, list, etc.).

---

## Why Use Dunder Methods?

Dunder methods help you:

* Customize object behavior
* Define how objects are printed
* Control operators like `+`, `-`, `==`
* Integrate your class naturally with Python syntax

---

## Commonly Used Dunder Methods

| Method     | Purpose                           |
| ---------- | --------------------------------- |
| `__init__` | Initializes object (constructor)  |
| `__str__`  | Defines string representation     |
| `__add__`  | Defines behavior for `+` operator |
| `__len__`  | Defines length of object          |
| `__eq__`   | Defines equality check            |

---

## `__init__` Example

Called automatically when an object is created.

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Ravi")
print(p.name)
```

---

## `__str__` Method

Controls what gets printed when an object is printed.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Animal name is {self.name}"

obj = Animal("Lion")
print(obj)
```

---

## `__add__` Method

Defines how the `+` operator behaves for objects.

### Reference Example (From Your Code)

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello how are you your name is {self.name}"

    def __add__(self, other):
        total = 0
        for i in other:
            total += i.age
        return f"Your sum of ages are {self.age + total}"
```

### Creating Objects

```python
obj1 = Animal("Lion", 12)
obj2 = Animal("Tiger", 15)
obj3 = Animal("Leopard", 20)

print(obj1 + (obj2, obj3))
```

### Output

```
Your sum of ages are 47
```

📌 **Note:**
To add more than two objects, the additional objects are passed as a **tuple**.

---

## How Python Calls Dunder Methods

```python
obj1 + obj2
```

Internally becomes:

```python
obj1.__add__(obj2)
```

---

## Important Notes

* Dunder methods are **not called directly**
* Python calls them automatically based on operations
* They improve readability and flexibility
* Overusing dunder methods can make code confusing — use wisely

---

## Key Takeaways

* Dunder methods customize class behavior
* `__init__` initializes objects
* `__str__` controls object printing
* `__add__` controls `+` operator behavior
* They make custom classes behave like built-in types
