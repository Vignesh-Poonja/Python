# Exception Handling in Python

## Introduction
Exception handling in Python allows programs to handle errors gracefully without crashing. By using `try-except` blocks, we can catch exceptions and respond appropriately.

## When to Use Exception Handling
- When handling invalid user input to prevent program crashes.
- When working with file operations to catch missing or inaccessible files.
- When dealing with network requests to handle connection failures.
- When executing code that interacts with external systems like databases or APIs.
- When debugging unexpected issues without exposing stack traces to users.

## Example: Listing Files in a Folder with Exception Handling
The following script takes a list of folder names as input and lists their contents, handling exceptions for missing or inaccessible folders.

```python
import os

folders = input("Please provide the list of folder names: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name!")
        break
    except PermissionError:
        print("No access to this: " + folder)
    else:
        print("--- Listing files for the folder: " + folder)
        for file in files:
            print(file)
```

## Explanation of Exception Handling
- `try`: The block where we attempt to execute code that may raise an exception.
- `except FileNotFoundError`: Catches cases where the specified folder does not exist.
- `except PermissionError`: Catches cases where the user lacks permission to access a folder.
- `else`: Executes only if no exceptions occur, ensuring that the folder contents are printed properly.

## Common Exceptions in Python
| Exception | Description |
|-----------|-------------|
| `FileNotFoundError` | Raised when a file or folder is not found. |
| `PermissionError` | Raised when access to a file or folder is denied. |
| `ZeroDivisionError` | Raised when division by zero occurs. |
| `ValueError` | Raised when a function receives an argument of the wrong type. |
| `TypeError` | Raised when an operation is performed on an incompatible type. |
| `KeyError` | Raised when accessing a non-existent dictionary key. |

## Best Practices for Exception Handling
- Always use specific exceptions instead of a generic `except` block.
- Use `finally` for cleanup operations like closing files or network connections.
- Avoid suppressing errors silently; log them for debugging purposes.
- Keep `try-except` blocks small to handle specific errors effectively.

Exception handling improves the robustness and reliability of Python programs by preventing unexpected crashes and enabling graceful error recovery.

