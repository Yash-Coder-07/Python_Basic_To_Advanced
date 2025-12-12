---

# 🟪 Python Dictionaries

## ⭐ What is a Dictionary?
A **dictionary** is a key–value data structure in Python.
It stores data in pairs like:

```
key → value
```

Dictionaries use curly braces **`{ }`**.

Example:

```python
student = {"name": "John", "age": 20}
```

---

# ⭐ Dictionary Powers (Properties)

### 🔹 1. Mutable

* You can change, add, or remove key-value pairs.

### 🔹 2. Unique Keys

* Keys must be unique.
* Values **can** be duplicates.

### 🔹 3. Insertion Ordered

* Dictionaries preserve the order in which items were added (Python 3.7+).

### 🔹 4. Fully Heterogeneous

* Keys and values can be of any data type:

```python
d = {1: "Hello", "x": 100, 3.5: [1, 2, 3], "info": {"city": "Mumbai"}}
```

---

# ⭐ Dictionary Syntax and Working

Accessing values using keys:

```python
student = {"name": "John", "age": 20}
print(student["name"])   # Output: John
```

You can perform **CRUD** operations (Create, Read, Update, Delete) on values,
but **keys cannot be changed once created** (only replaced by deleting and re-adding).

---

# ⭐ Dictionary Traversing

### Looping through keys:

```python
numbers = {1: 10, 2: 20, 3: 30}

for k in numbers:
    print(k, numbers[k])
```

### Looping through values:

```python
for val in numbers.values():
    print(val)
```

### Looping through key–value pairs:

```python
for k, v in numbers.items():
    print(k, v)
```

---

# ⭐ Dictionary Methods

Let:

```python
d = {10: 100, 20: 200, 30: 300}
```

### ✔ `d.get(key)`

Returns value of key (returns `None` if key is missing).

```python
d.get(20)   # 200
```

### ✔ `d.update({key: value})`

Adds or updates a key-value pair.

```python
d.update({40: 400})
```

### ✔ Add new key-value directly

```python
d[50] = 500
```

### ✔ Deleting items

```python
del d[30]
d.__delitem__(20)   # alternate
```

### ✔ `d.clear()`

Removes all elements.

### ✔ Copying Dictionaries

* `copy()` → **shallow copy** (independent)
* `b = d` → **deep reference** (changes reflect in both)

---

# ⭐ CRUD Examples

### Update value:

```python
d[10] = 1000
```

### Add new key:

```python
d[60] = 600
```

### Delete:

```python
del d[40]
```

---

# ⭐ Dictionary Interview Questions

1. Write a Python script to merge two dictionaries.
2. Write a Python program to sum all values in a dictionary.
3. Count frequency of each element in a list using a dictionary.
4. Combine two dictionaries by adding values of common keys.
5. Convert two lists into one dictionary.

---

# ⭐ Example Code from Your Notes

```python
d = {10:100, 20:200, 30:300, 40:400}

# Access
print(d[20])

# Update
d[10] = 1000

# Add new key
d[50] = 500

# Delete
del d[40]

# Traversing
for i in d:
    print(i, d[i])

# Values only
for val in d.values():
    print(val)

# Methods
b = d.copy()
print(d.get(30))
```

---
