# *args and **kwargs in Python

## What are `*args` and `**kwargs`?

`*args` and `**kwargs` are special syntax used in Python functions to accept a **variable number of arguments**.

* You **don’t have to use the exact names** `args` and `kwargs
* The important part is:

  * `*` → positional arguments
  * `**` → keyword arguments

---

## Why Use `*args` and `**kwargs`?

They are useful when:

* You don’t know how many arguments will be passed
* Writing flexible functions
* Building decorators, APIs, frameworks
* Avoiding repeated parameters

---

## `*args` (Variable Positional Arguments)

* Used for **multiple positional arguments**
* Collected as a **tuple**
* Single star `*` is mandatory

### Example

```python
def fun(*args):
    print(args)

fun(1, 2, 3)
```

### Output

```
(1, 2, 3)
```

---

## `**kwargs` (Variable Keyword Arguments)

* Used for **multiple key–value arguments**
* Collected as a **dictionary**
* Double star `**` is mandatory

### Example

```python
def info(**kwargs):
    print(kwargs)

info(name="Yash", age=20)
```

### Output

```
{'name': 'Yash', 'age': 20}
```

---

## Using `*args` and `**kwargs Together

```python
def fun(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

fun(1, 2, 3, name="Arin", age=21)
```

---

## `*args` with Decorators (From Reference Code)

### Decorator Definition

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Your given number addition is:")
        func(*args, **kwargs)
        print("Thank You....")
    return wrapper
```

### Function Using `*args`

```python
@decorator
def addition(*args):
    total = 0
    for i in args:
        total += i
    print(f"Sum is {total}")
```

### Calling the Function

```python
addition(12, 12, 13, 78, 98, 6, 5, 4, 7, 8, 2, 152, 2, 5)
```

---

## `**kwargs` Example (From Reference Code)

```python
def information(**kwargs):
    print("Your information is:\n")
    for key in kwargs:
        print(f"{key} : {kwargs[key]}")

information(name="Yash", age=20, designation="AI/ML Engineer")
```

---

## Key Differences Between `*args` and `**kwargs`

| Feature   | `*args`         | `**kwargs`     |
| --------- | --------------- | -------------- |
| Type      | Tuple           | Dictionary     |
| Arguments | Positional      | Keyword        |
| Symbol    | `*`             | `**`           |
| Use Case  | Multiple values | Key–value data |

---

## Important Notes

* Order matters in function definition:

  ```python
  def func(a, *args, **kwargs):
      pass
  ```
* `*args` must come before `**kwargs`
* Commonly used in decorators and frameworks

---

## Key Takeaways

* `*args` → flexible positional arguments
* `**kwargs` → flexible keyword arguments
* Both make functions reusable and scalable
* Essential for decorators and advanced Python
