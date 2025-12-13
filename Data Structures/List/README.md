# 🟩 Python Lists

## ⭐ What is a List?

A **list** is an ordered, mutable collection in Python that allows duplicates and stores multiple data types.
Lists are created using **square brackets `[ ]`**.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40]
```

---

## ⭐ List Properties

### 🔹 1. Mutable

* List elements **can be changed** after creation.

```python
nums = [10, 20, 30]
nums[1] = 99   # [10, 99, 30]
```

### 🔹 2. Allows Duplicates

```python
l = [1, 2, 2, 3]
```

### 🔹 3. Ordered

* Elements maintain the order in which they were inserted.
* Supports indexing and slicing.

### 🔹 4. Heterogeneous

* A list can store different data types.

```python
mix = [10, "hello", 3.5, True]
```

---

# ⭐ Indexing & Slicing

### Indexing

```python
nums = [10, 20, 30]
nums[0]    # 10
nums[-1]   # 30
```

### Slicing

```python
nums[0:2]   # [10, 20]
nums[1:]    # [20, 30]
```

---

# ⭐ List Traversing

### Using Index

```python
for i in range(len(nums)):
    print(nums[i])
```

### Direct Traversal

```python
for x in nums:
    print(x)
```

---

# ⭐ Important List Methods

Given:

```python
numbers = [5, 2, 9, 1, 5, 6]
```

### ✔ `append(x)`

Adds `x` to the end.

### ✔ `insert(i, x)`

Inserts `x` at index `i`.

### ✔ `extend(iterable)`

Adds multiple items.

```python
numbers.extend([20, 25, 30])
```

### ✔ `remove(x)`

Removes the first occurrence of `x`.

### ✔ `pop(i)`

Removes and returns element at index `i`.

### ✔ `index(x)`

Returns index of first occurrence of `x`.

### ✔ `count(x)`

Counts occurrences of `x`.

### ✔ `sort()`

Sorts the list in ascending order.

### ✔ `reverse()`

Reverses the list.

### ✔ `copy()`

Creates a shallow copy of the list.

### ✔ `clear()`

Removes all elements.

---

# ⭐ Example Code

```python
numbers = [5, 2, 9, 1, 5, 6]

numbers.append(10)
numbers.insert(2, 15)
numbers.extend([20, 25, 30])

numbers.remove(5)
popped_item = numbers.pop(3)

index_val = numbers.index(6)
count_5 = numbers.count(5)

numbers.sort()
numbers.reverse()

new_numbers = numbers.copy()
numbers.clear()
```

