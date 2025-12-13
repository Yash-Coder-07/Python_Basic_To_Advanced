# 🟦 Python Tuples

## ⭐ What is a Tuple?

A **tuple** is an ordered collection in Python that is **immutable** (cannot be changed after creation).
Tuples use **parentheses `( )`**.

```python
t = (1, 2, 3, 4)
```

---

## ⭐ Tuple Properties

### 🔹 1. Immutable

* You cannot modify, insert, or delete elements after the tuple is created.

### 🔹 2. Allows Duplicates

```python
t = (1, 2, 2, 3)
```

### 🔹 3. Ordered

* Elements maintain insertion order.
* Indexing is allowed.

### 🔹 4. Heterogeneous

* Can store different data types.

```python
b = (1, 2, 3, 5, 5, 6.7, 89, "Hello", True)
```

---

# ⭐ Tuple Traversing

### Using Index

```python
t = (5, 10, 15)

for i in range(len(t)):
    print(t[i])
```

### Direct Traversal

```python
for x in t:
    print(x)
```

---

# ⭐ Important Tuple Methods

Given:

```python
t = (5, 2, 9, 1, 5, 6)
```

### ✔ `index(x)`

Returns the index of first occurrence of `x`.

```python
t.index(9)   # Output: 2
```

### ✔ `count(x)`

Counts occurrences of `x`.

```python
t.count(5)   # Output: 2
```

> Tuples have only **two** main methods: `index()` and `count()`.

---

# ⭐ Tuple Unpacking

```python
a, b, c, d = (1, 2, 3, 4)

print(b)      # 2
print(type(b))  # int
```

Each variable stores its corresponding tuple value.

---

# ⭐ Single Element Tuple (VERY Important)

❌ Not a tuple:

```python
a = (1)
# type → int
```

✔ Correct one-element tuple:

```python
a = (1,)
# type → tuple
```

The comma **defines** it as a tuple.

---

# ⭐ Example Code

```python
a = (1, 2, 3, 4)
print(type(a))

b = (1, 2, 3, 5, 5, 6.7, 89, "Hello", True)
print(b)

index_value = b.index(6.7)
print(index_value)

count_value = b.count(5)
print(count_value)

# Tuple Unpacking
a, b, c, d = (1, 2, 3, 4)
print(b)
print(type(b))

# Single Element Tuple
a = (1,)
print(type(a))
```
