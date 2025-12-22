# Decorators in Python

## What is a Decorator?

A **decorator** is a function that **modifies another function’s behavior** without changing its actual code.

👉 Think of it like:

* Function = cake
* Decorator = icing on the cake
  The cake remains the same, but decorators **add extra behavior**.

---

## Why Use Decorators?

* Add functionality **before or after** a function runs
* Avoid code duplication
* Keep code clean and readable
* Commonly used for logging, authentication, validation, timing, etc.

---

## Basic Decorator Structure

A decorator consists of:

1. An outer function (decorator)
2. An inner function (wrapper)
3. Returning the wrapper

```python
def my_decorator(func):
    def wrapper():
        print("Something before the function runs")
        func()
        print("Something after the function runs")
    return wrapper
```

---

## Using a Decorator

```python
@my_decorator
def say_hello():
    print("Hello")

say_hello()
```

### Output

```
Something before the function runs
Hello
Something after the function runs
```

---

## How Decorators Work

```python
@decorate
def hello():
    print("Hello I am Yash")
```

This is internally equivalent to:

```python
hello = decorate(hello)
```

---

## Decorator Example (From Reference Code)

```python
def decorate(func):
    def wrapper():
        print("I will print myself before hello function")
        func()
        print("I will print after function")
    return wrapper

@decorate
def hello():
    print("Hello I am Yash")

hello()
```

---

## Decorators with Arguments

When the decorated function takes parameters, the wrapper must also accept parameters.

```python
def decorate(func):
    def wrapper(a, b):
        print("Addition of your number is:")
        func(a, b)
        print("Thank You...")
    return wrapper
```

### Applying the Decorator

```python
@decorate
def add(a, b):
    print(f"Addition of two numbers is {a + b}")

add(5, 8)
```

---

## `@property` Decorator

The `@property` decorator allows you to **access a method like an attribute**.

```python
class Animal:
    @property
    def show(self):
        print("Hello how are you")

obj = Animal()
obj.show   # No parentheses needed
```

---

## Important Notes

* Decorators are executed **at function definition time**
* Wrapper function controls execution flow
* For flexible decorators, use `*args` and `**kwargs`
* Decorators are heavily used in frameworks (Flask, Django)

---

## Key Takeaways

* Decorators modify functions without changing their code
* Use `@decorator_name` syntax
* Wrapper function controls behavior
* `@property` converts methods into attributes
* Essential concept for advanced Python

