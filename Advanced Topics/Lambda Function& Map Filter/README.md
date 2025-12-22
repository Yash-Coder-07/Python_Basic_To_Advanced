# Lambda Functions, `map()`, `filter()`, and `zip()` in Python

## Lambda Functions

### What is a Lambda Function?

A **lambda function** is an **anonymous, inline function** defined using the `lambda` keyword.

* Used for **short and simple operations**
* Often written where a function is needed **only once**
* Can take **multiple arguments**, but must contain **only one expression**

---

### Lambda Syntax

```python
lambda arguments: expression
```

---

### Basic Example

```python
square = lambda x: x ** 2
print(square(4))   # Output: 16
```

---

### Lambda with Multiple Arguments

```python
addition = lambda a, b: a + b
print(addition(6, 9))
```

---

### Lambda with Conditional Expression

```python
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(7))   # Output: Odd
```

---

## `map()` Function

### What is `map()`?

`map()` applies a function to **each element** of an iterable.

* Returns a **map object** (convert to list if needed)
* Does **not filter** items
* Can use **lambda or normal functions**

### Syntax

```python
map(function, iterable)
```

---

### Example Using Lambda

```python
numbers = [1, 2, 3, 4]
doubled = map(lambda x: x * 2, numbers)
print(list(doubled))   # Output: [2, 4, 6, 8]
```

---

### Example Using Normal Function

```python
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4]
result = map(square, numbers)
print(list(result))
```

---

## `filter()` Function

### What is `filter()`?

`filter()` selects elements from an iterable **based on a condition**.

* Keeps only items that return **True**
* Returns a **filter object**
* Used for filtering data

### Syntax

```python
filter(function, iterable)
```

---

### Example Using Lambda

```python
numbers = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))   # Output: [2, 4]
```

---

### Example Using Normal Function (From Reference Code)

```python
def even(x):
    return x % 2 == 0

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(even, a)
print(list(result))
```

---

## `zip()` Function

### What is `zip()`?

`zip()` combines multiple iterables **element-wise** into tuples.

### Example

```python
names = ["A", "B", "C"]
scores = [90, 85, 88]

zipped = zip(names, scores)
print(list(zipped))
```

### Output

```
[('A', 90), ('B', 85), ('C', 88)]
```

---

## Differences Between `map()` and `filter()`

| Feature       | `map()`         | `filter()`      |
| ------------- | --------------- | --------------- |
| Purpose       | Transform items | Select items    |
| Removes items | ❌ No            | ✅ Yes           |
| Output        | Modified values | Filtered values |
| Return type   | map object      | filter object   |

---

## Key Takeaways

* Lambda functions are short, anonymous functions
* `map()` transforms each item in an iterable
* `filter()` removes unwanted items based on a condition
* `zip()` combines multiple iterables
* Convert map/filter/zip objects to list for output

