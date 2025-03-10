# Python Dictionaries and Sets

## Introduction
Dictionaries and sets are essential data structures in Python that help in storing and managing collections of data efficiently.

## When to Use Dictionaries and Sets
- **Dictionaries** should be used when you need to store key-value pairs and perform fast lookups.
- **Sets** should be used when you need to store unique elements and perform fast membership tests.
- Use dictionaries when working with structured data that requires easy access using keys.
- Use sets for mathematical operations like union, intersection, and difference.
- Both are useful for improving performance in searching and organizing data.

## Python Dictionaries
Dictionaries store data as key-value pairs and allow efficient lookups.

### Creating a Dictionary
```python
dict_example = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
```

### Accessing Values
```python
print(dict_example["name"])  # Output: Alice
```

### Adding and Updating Values
```python
dict_example["age"] = 26  # Update value
dict_example["country"] = "USA"  # Add new key-value pair
```

### Removing Elements
```python
del dict_example["city"]  # Remove a key-value pair
```

### Iterating Through a Dictionary
```python
for key, value in dict_example.items():
    print(key, "->", value)
```

### Dictionary Methods
- `keys()`, `values()`, `items()` – Retrieve keys, values, or key-value pairs.
- `get(key, default)` – Get a value safely without KeyError.
- `pop(key)` – Remove a key and return its value.

## Python Sets
Sets store unique elements and allow fast membership checks.

### Creating a Set
```python
set_example = {1, 2, 3, 4, 5}
```

### Adding Elements
```python
set_example.add(6)
```

### Removing Elements
```python
set_example.remove(3)  # Removes 3 if it exists, else raises an error
set_example.discard(10)  # Removes 10 if it exists, else does nothing
```

### Set Operations
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)  # Union: {1, 2, 3, 4, 5}
print(set1 & set2)  # Intersection: {3}
print(set1 - set2)  # Difference: {1, 2}
print(set1 ^ set2)  # Symmetric Difference: {1, 2, 4, 5}
```

## Best Practices
- Use dictionaries when you need fast lookups with meaningful keys.
- Use sets when working with unique elements and mathematical operations.
- Avoid modifying dictionaries while iterating over them.
- Use `defaultdict` from `collections` when handling missing dictionary keys.

Dictionaries and sets provide powerful and efficient ways to handle data in Python. 🚀

