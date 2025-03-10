# Data Types in Python

## Introduction

Python provides various built-in data types to store and manipulate different kinds of data. Understanding these data types is essential for writing efficient and error-free Python programs.

---

## 1. Numeric Types

### a) Integer (`int`)

- Used to store whole numbers.
- Example:
  ```python
  x = 10
  print(type(x))  # Output: <class 'int'>
  ```

### b) Floating-Point (`float`)

- Used to store decimal numbers.
- Example:
  ```python
  y = 10.5
  print(type(y))  # Output: <class 'float'>
  ```

### c) Complex (`complex`)

- Used to store complex numbers with a real and imaginary part.
- Example:
  ```python
  z = 2 + 3j
  print(type(z))  # Output: <class 'complex'>
  ```

---

## 2. Sequence Types

### a) String (`str`)

- Used to store a sequence of characters.
- Example:
  ```python
  text = "Hello, Python!"
  print(type(text))  # Output: <class 'str'>
  ```

### b) List (`list`)

- A mutable ordered collection of elements.
- Example:
  ```python
  my_list = [1, 2, 3, "Python"]
  print(type(my_list))  # Output: <class 'list'>
  ```

### c) Tuple (`tuple`)

- An immutable ordered collection of elements.
- Example:
  ```python
  my_tuple = (1, 2, 3, "Python")
  print(type(my_tuple))  # Output: <class 'tuple'>
  ```

---

## 3. Set Types

### a) Set (`set`)

- A collection of unique unordered elements.
- Example:
  ```python
  my_set = {1, 2, 3, 4}
  print(type(my_set))  # Output: <class 'set'>
  ```

### b) Frozen Set (`frozenset`)

- Similar to a set but immutable.
- Example:
  ```python
  my_frozenset = frozenset([1, 2, 3, 4])
  print(type(my_frozenset))  # Output: <class 'frozenset'>
  ```

---

## 4. Mapping Type

### Dictionary (`dict`)

- A collection of key-value pairs.
- Example:
  ```python
  my_dict = {"name": "Alice", "age": 25}
  print(type(my_dict))  # Output: <class 'dict'>
  ```

---

## 5. Boolean Type

### Boolean (`bool`)

- Represents `True` or `False`.
- Example:
  ```python
  is_python_fun = True
  print(type(is_python_fun))  # Output: <class 'bool'>
  ```

---

## 6. None Type

### NoneType (`None`)

- Represents the absence of a value.
- Example:
  ```python
  value = None
  print(type(value))  # Output: <class 'NoneType'>
  ```

---

## When to Use Different Data Types

- **Numeric types** are used for mathematical operations.
- **Strings** are used for text processing.
- **Lists and tuples** are used to store ordered collections of elements.
- **Sets** are useful when uniqueness of elements is required.
- **Dictionaries** are ideal for storing key-value pairs.
- **Boolean types** are used for conditional checks and logic.
- **NoneType** is used for defining variables with no assigned value.

### Summary Table

| Data Type   | Mutability | Ordered | Example                |
| ----------- | ---------- | ------- | ---------------------- |
| `int`       | Immutable  | N/A     | `10`                   |
| `float`     | Immutable  | N/A     | `10.5`                 |
| `complex`   | Immutable  | N/A     | `2 + 3j`               |
| `str`       | Immutable  | Yes     | `'Hello'`              |
| `list`      | Mutable    | Yes     | `[1, 2, 3]`            |
| `tuple`     | Immutable  | Yes     | `(1, 2, 3)`            |
| `set`       | Mutable    | No      | `{1, 2, 3}`            |
| `frozenset` | Immutable  | No      | `frozenset({1, 2, 3})` |
| `dict`      | Mutable    | No      | `{"name": "Alice"}`    |
| `bool`      | Immutable  | N/A     | `True` / `False`       |
| `NoneType`  | N/A        | N/A     | `None`                 |

---

## Conclusion

Understanding Python's data types allows you to select the appropriate type for your variables and optimize memory and performance effectively. Happy coding! 

