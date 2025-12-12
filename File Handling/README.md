# File Handling in Python

## What Are Files?

* Any name with an extension (e.g., `.py`, `.txt`, `.mp3`) is considered a file.
* To work with such files in Python, we use **file handling**.

---

## File Handling

File handling refers to performing CRUD operations on files:

* **C**reate
* **R**ead
* **U**pdate (Write/Rewrite)
* **D**elete

Python provides the `open()` function to work with files.

---

## File Modes

| Mode | Description                                               |
| ---- | --------------------------------------------------------- |
| `r`  | Read (default). File must exist.                          |
| `w`  | Write. Creates a new file or overwrites an existing file. |
| `a`  | Append. Adds content to the end of the file.              |
| `x`  | Create. Creates a new file; raises error if file exists.  |

---

## Basic Syntax

### Opening and Reading a File

```python
file = open("myfile.txt", "r")

print(file.read())       # Read entire file
# print(file.readline()) # Read one line
# print(file.readlines())# Read all lines as a list

file.close()
```

* `read()` → reads the full content
* `readline()` → reads one line
* `readlines()` → returns a list of all lines

---

## Using `with` (Recommended)

Python provides a cleaner way to handle files using `with`.
It automatically closes the file after execution.

```python
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
```

---

## Writing to a File

### Using `w` (overwrite/create)

```python
f = open("superman.txt", "w")
f.write("Hello, this is Yash and I am writing inside this file.")
f.close()
```

`w` removes existing content.

---

## Appending to a File

### Using `a` (append)

```python
f = open("superman.txt", "a")
f.write(" Now I am appending more content.")
f.close()
```

---

## Creating a New File

### Using `x`

```python
f = open("newfile.txt", "x")
```

Fails if the file already exists.

---
