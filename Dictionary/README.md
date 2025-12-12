content: |
  # 🟪 Python Dictionaries

  ## ⭐ What is a Dictionary?

  A **dictionary** is a key–value data structure in Python.
  It stores data in pairs like:

      key → value

  Dictionaries use curly braces `{ }`.

  Example:

      student = {"name": "John", "age": 20}

  ---

  # ⭐ Dictionary Powers (Properties)

  ### 🔹 1. Mutable
  - You can change, add, or remove key-value pairs.

  ### 🔹 2. Unique Keys
  - Keys must be unique.
  - Values can be duplicates.

  ### 🔹 3. Insertion Ordered
  - Dictionaries preserve insertion order (Python 3.7+).

  ### 🔹 4. Fully Heterogeneous
  - Keys and values can be any data type:

      d = {1: "Hello", "x": 100, 3.5: [1, 2, 3], "info": {"city": "Mumbai"}}

  ---

  # ⭐ Dictionary Syntax and Working

      student = {"name": "John", "age": 20}
      print(student["name"])   # Output: John

  Keys cannot be changed once created.

  ---

  # ⭐ Dictionary Traversing

  ### Loop through keys:
      for k in numbers:
          print(k, numbers[k])

  ### Loop through values:
      for val in numbers.values():
          print(val)

  ### Loop through key–value pairs:
      for k, v in numbers.items():
          print(k, v)

  ---

  # ⭐ Dictionary Methods

      d = {10: 100, 20: 200, 30: 300}

  ✔ d.get(key)  
  ✔ d.update({key: value})  
  ✔ d[key] = value  
  ✔ del d[key]  
  ✔ d.clear()  
  ✔ d.copy()  

  ---

  # ⭐ CRUD Examples

      d[10] = 1000
      d[60] = 600
      del d[40]

  ---

  # ⭐ Dictionary Interview Questions

  - Merge two dictionaries  
  - Sum all values  
  - Count frequency of list elements  
  - Combine dictionaries by adding values  
  - Convert lists to dictionary  

  ---

  # ⭐ Example Code

      d = {10:100, 20:200, 30:300, 40:400}

      print(d[20])
      d[10] = 1000
      d[50] = 500
      del d[40]

      for i in d:
          print(i, d[i])

      for val in d.values():
          print(val)

      b = d.copy()
      print(d.get(30))
