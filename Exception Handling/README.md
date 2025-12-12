# Exception Handling in Python

## Errors

Errors occur due to mistakes in the code that prevent it from running. These may be syntax errors or logical errors.

### Syntax Error

Occurs when the Python syntax is incorrect.

```python
print("Hello World"   # Missing closing parenthesis
```

### Indentation Error

Occurs when indentation rules are not followed.

```python
def func():
print("Hello")    # No indentation
```

* Mixing tabs and spaces can also cause indentation issues.
* Syntax and indentation errors **cannot be handled** at runtime.

---

## Exceptions

Exceptions are unexpected events or errors that occur during the execution of a program, disrupting the normal flow.

Example:

```python
print("Start")
print(10 / 0)  # Raises ZeroDivisionError
print("End")   # This line will not run
```

---

## Exception Handling Keywords

| Keyword     | Purpose                                |
| ----------- | -------------------------------------- |
| **try**     | Wraps code that may cause an exception |
| **except**  | Handles the exception if it occurs     |
| **else**    | Runs only if no exception occurs       |
| **finally** | Runs no matter what (exception or not) |
| **raise**   | Manually raises an exception           |

---

## Example: Basic Exception Handling

```python
a = int(input("Tell your number: "))

try:
    print(10 / a)
except Exception as err:
    print(f"Sorry, there is an error: {err}")
else:
    print("Good, there is no exception")
finally:
    print("I will run no matter what")

print("Execution continues...")
```

---

## Using `raise`

`raise` is used to manually throw an exception.
When raising your own exceptions, you typically use `try-except` to handle them.

### Example:

```python
age = int(input("Tell your age: "))

try:
    if age < 10 or age > 18:
        raise ValueError("Your age must be between 10 and 18")
    else:
        print("Welcome to the club")

except Exception as err:
    print(f"Error occurred: {err}")

print("Club will start soon...")
```

---

