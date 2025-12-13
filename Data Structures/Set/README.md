# 🟧 Python Sets

## ⭐ What is a Set?

A **set** is an unordered collection of unique elements in Python.
Sets are created using **curly braces `{ }`** or the `set()` constructor.

```python
a = {1, 2, 3, 4}
```

---

# ⭐ Set Properties

### 🔹 1. Mutable

* You can add or remove elements using set methods.

### 🔹 2. No Duplicates

* All elements must be unique.

```python
s = {1, 2, 2, 3}   # becomes {1, 2, 3}
```

### 🔹 3. Unordered

* Sets do **not maintain order**, so indexing is not allowed.
* Traversing gives elements in random order.

### 🔹 4. Semi-Heterogeneous

* Sets can store **numbers, strings, tuples** (hashable data types).
* **Cannot store lists or dictionaries** (because they are mutable & not hashable).

```python
s = {1, 2, "hello", (1, 2)}
```

---

# ⭐ How Python Stores Set Elements (Important Concept)

* Each element is stored based on its **hash value**.
* The `hash()` function determines where the value is stored in memory.
* Because hashing does not keep order → sets are unordered.
* Only **immutable (hashable)** objects are allowed inside a set.

---

# ⭐ Set Traversing

Since sets are unordered and have no index, traversal is done directly:

```python
a = {1, 2, 3, 4, 5}
for i in a:
    print(i)       # prints in random order
```

---

# ⭐ Important Set Methods

Given:

```python
s = {1, 2, 3}
```

### ✔ `add(x)`

Adds an element.

```python
s.add(4)
```

### ✔ `remove(x)`

Removes x → raises error if not found.

### ✔ `discard(x)`

Removes x → **no error** if x does not exist.

### ✔ `pop()`

Removes a **random** element.

### ✔ `clear()`

Removes all elements from the set.

---

# ⭐ Set Operations (Very Important for Interviews)

Given:

```python
A = {1, 2, 3}
B = {3, 4, 5}
```

### ✔ Union

All unique elements from both sets.

```python
A.union(B)     # {1, 2, 3, 4, 5}
```

Shortcut:

```python
A | B
```

### ✔ Intersection

Common elements.

```python
A.intersection(B)   # {3}
```

Shortcut:

```python
A & B
```

### ✔ Difference

Elements in A but not in B.

```python
A.difference(B)     # {1, 2}
```

Shortcut:

```python
A - B
```

### ✔ Symmetric Difference

Elements that are unique to each set.

```python
A.symmetric_difference(B)   # {1, 2, 4, 5}
```

Shortcut:

```python
A ^ B
```

---

# ⭐ Example Code from Your Notes

```python
b = {1, 2, 3, 4, 5}
c = {3, 4, 5, 6, 7}

print(b.union(c))
print(b.intersection(c))
print(b.difference(c))
print(b.symmetric_difference(c))
```

---

# ⭐ Notes on Errors & Restrictions

* `b.remove(x)` will cause **error** if x does not exist.
* `b.discard(x)` will **not** cause error.
* Sets **cannot contain**:

  * lists
  * dictionaries
  * other mutable objects

---

# ⭐ Important Takeaway

Sets are powerful for mathematical operations but **not commonly used** for day-to-day list-like storage because they lack indexing and order.

---
