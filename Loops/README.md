# Loops, Break, and Continue in Python

## Introduction
Loops in Python are used to execute a block of code repeatedly. The `break` and `continue` statements provide more control over loop execution.

## When to Use Loops
- When iterating over sequences like lists, tuples, or strings.
- When executing a block of code a specific number of times.
- When automating repetitive tasks.
- When processing large datasets efficiently.

## Types of Loops in Python

### 1. `for` Loop
Used for iterating over sequences like lists, tuples, and strings.

#### Example:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### 2. `while` Loop
Executes as long as a given condition is `True`.

#### Example:
```python
count = 0
while count < 5:
    print("Count is:", count)
    count += 1
```

## `break` Statement
The `break` statement is used to exit a loop when a condition is met.

#### Example:
```python
for number in range(10):
    if number == 5:
        print("Breaking the loop at", number)
        break
    print(number)
```

## `continue` Statement
The `continue` statement skips the current iteration and moves to the next one.

#### Example:
```python
for number in range(5):
    if number == 2:
        continue  # Skip 2 and continue with the next iteration
    print(number)
```

## Best Practices
- Use `for` loops when iterating over known sequences.
- Use `while` loops when the number of iterations is unknown.
- Use `break` to exit loops early when necessary.
- Use `continue` to skip specific iterations when required.
- Avoid infinite loops unless explicitly needed.

Loops are fundamental in Python programming and allow for efficient iteration and automation.

