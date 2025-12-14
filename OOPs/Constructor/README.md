## Constructor in Python

### What is a Constructor?

A **constructor** is a special method that:

* Runs automatically when an object is created
* Is used to initialize object data
* Defined using `__init__()`

---

### Constructor Example

```python
class Student:
    def __init__(self, name):
        self.name = name   # Instance attribute

s = Student("Riya")
print(s.name)
```

* `self` refers to the **current object**
* Each object gets its own memory location

---

## Example: Factory Class with Constructor

```python
class Factory:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(f"Material: {self.material}, Zips: {self.zips}, Pockets: {self.pockets}")
```

### Creating Objects

```python
reebok = Factory("Leather", 3, 2)
campus = Factory("Waterproof", 4, 3)

reebok.show()
campus.show()
```

* `self` targets the specific object’s data
* Each object maintains its own state

---

## Key Takeaways

* Class → Blueprint
* Object → Real instance of class
* Constructor → Initializes object data
* `self` → Refers to current object
* OOPS helps build scalable and maintainable programs

---