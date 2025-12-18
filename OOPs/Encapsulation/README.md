# Encapsulation in Python (OOPS)

## What is Encapsulation?

Encapsulation means **binding data (variables) and code (methods) together** inside a single unit — a **class**.

It also refers to **hiding internal implementation details** and exposing only what is necessary.

### Benefits of Encapsulation

* Prevents data from being changed accidentally
* Keeps code clean and easy to use
* Provides control over what can be accessed or modified
* Improves maintainability and security

---

## Access Modifiers in Python

Access modifiers define **how attributes and methods can be accessed**.

Python supports **three types of access modifiers** (by convention):

---

## 1. Public Members

* Default access level
* Accessible **from anywhere** (inside or outside the class)

```python
class Demo:
    def __init__(self):
        self.name = "Public Member"
```

---

## 2. Protected Members

* Created using a **single underscore (`_`)**
* Accessible outside the class, but **intended for internal use**
* Python does **not enforce** protection (convention only)

```python
class Factory:
    _location = "Pune"

    def _show(self):
        print("Protected method")
```

### Accessing Protected Members (Not Recommended)

```python
class Bhopal(Factory):
    def show(self):
        print(self._location)

obj = Bhopal()
obj.show()
```

---

## 3. Private Members

* Created using **double underscore (`__`)**
* Cannot be accessed directly from outside the class
* Python uses **name mangling** to restrict access

```python
class Demo:
    def __init__(self):
        self.__salary = 50000
```

❌ Not Accessible:

```python
obj = Demo()
# obj.__salary  # Error
```

---

## Private Members Example (From Reference Code)

```python
class Factory:
    __a = "Pune"   # Private attribute

    def show(self):
        print(Factory.__a)  # Accessible only inside class

obj = Factory()
obj.show()
```

* Private members can be accessed **inside the class**
* They cannot be accessed or modified directly from outside

---

## Important Notes

* Python does **not enforce strict access control**
* Access modifiers are based on **naming conventions**
* Private members are name-mangled to prevent accidental access
* Encapsulation focuses on **data protection, not restriction**

---

## Comparison of Access Modifiers

| Access Type | Symbol | Accessible Outside | Purpose      |
| ----------- | ------ | ------------------ | ------------ |
| Public      | None   | Yes                | Open access  |
| Protected   | `_`    | Yes (convention)   | Internal use |
| Private     | `__`   | No (directly)      | Data hiding  |

---

## Key Takeaways

* Encapsulation binds data and behavior together
* Use public members for general access
* Use protected members for internal or inherited usage
* Use private members to hide sensitive data
* Python uses **convention**, not strict enforcement
