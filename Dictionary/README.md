# Python Dictionary — Notes

## What is a Dictionary?

A dictionary in Python is a collection of key–value pairs.
It uses the syntax:

```
key: value
```

Example:

```python
student = {"name": "John", "age": 20}
```

---

## Dictionary Features

### 1. Mutable

* You can add, update, or delete key–value pairs.
* Keys cannot be changed, only values can.

### 2. Keys Must Be Unique

* Duplicate keys are not allowed.
* Duplicate values are allowed.

### 3. Maintains Insertion Order

* Python dictionaries preserve the order of insertion.

### 4. Heterogeneous

* Keys and values can be of any datatype, including lists or other dictionaries.

---

## Dictionary Syntax

### Creating a Dictionary

```python
student = {"name": "John", "age": 20}
```

### Accessing Values

```python
print(student["name"])  # Output: John
```

---

## CRUD Operations

### Update Value

```python
student["age"] = 21
```

### Add New Key–Value Pair

```python
student["city"] = "Pune"
```

### Using update()

```python
student.update({"grade": "A"})
```

### Delete Items

```python
del student["age"]
student.__delitem__("name")
```

---

## Traversing a Dictionary

### Loop Over Keys

```python
d = {10: 100, 20: 200, 30: 300}

for key in d:
    print(key, d[key])
```

### Loop Over Values

```python
for value in d.values():
    print(value)
```

### Loop Over Key–Value Pairs

```python
for k, v in d.items():
    print(k, v)
```

---

## Common Dictionary Methods

| Method          | Description             |
| --------------- | ----------------------- |
| `clear()`       | Removes all items       |
| `copy()`        | Returns a shallow copy  |
| `get(key)`      | Returns value safely    |
| `items()`       | Returns key–value pairs |
| `keys()`        | Returns all keys        |
| `values()`      | Returns all values      |
| `update({...})` | Adds or updates items   |

### Shallow Copy vs Deep Copy

```python
b = d.copy()   # Shallow copy
b = d          # Deep copy (same reference)
```

---

## Practice Questions

1. Merge two Python dictionaries.
2. Sum all values in a dictionary.
3. Count frequency of elements using a dictionary.
4. Combine two dictionaries by adding values of common keys.

---

## Example Codes

### Merge Two Dictionaries

```python
d1 = {1: 10, 2: 20}
d2 = {2: 30, 3: 40}

merged = {**d1, **d2}
print(merged)
```

### Sum of Dictionary Values

```python
d = {1: 10, 2: 20, 3: 30}
print(sum(d.values()))
```

---


Just tell me!

