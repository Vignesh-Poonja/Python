# File Handling in Python

## Introduction
File handling in Python allows reading, writing, and modifying files efficiently. This is essential for working with configuration files, logs, databases, and other data storage.

## When to Use File Handling
- When reading and writing configuration files.
- When storing logs for debugging and monitoring purposes.
- When processing large datasets from files.
- When updating structured data without using databases.

## Example: Updating a Server Configuration File
The following function reads a configuration file, modifies a specific key's value, and writes the changes back to the file.

### Python Code
```python
def update_server_config(file_path, key, value):
    with open(file_path, 'r') as file:  # Open the file in read mode
        lines = file.readlines()

    with open(file_path, 'w') as file:  # Open the file in write mode
        for line in lines:
            if key in line:
                file.write(key + '=' + value + '\n')
            else:
                file.write(line)

# Updating server configuration
update_server_config("server.conf", "MAX_CONNECTIONS", "500")
update_server_config("server.conf", "TIMEOUT", "60")

# Another way to update the config
file_path = "server.conf"
key = "PORT"
value = "8081"
update_server_config(file_path, key, value)
```

## Example: Server Configuration File
A sample `server.conf` file before and after modification.

### Sample Configuration File (`server.conf`)
```
# Server Configuration File

# Network Settings
PORT=8081
MAX_CONNECTIONS=500
TIMEOUT=60

# Security Settings
SSL_ENABLED = true
SSL_CERT = /path/to/certificate.pem

# Logging Settings
LOG_LEVEL = INFO
LOG_FILE = /var/log/server.log

# Other Settings
ENABLE_FEATURE_X = true
```

## File Handling Modes in Python
| Mode | Description |
|------|-------------|
| `r`  | Read mode (default). File must exist. |
| `w`  | Write mode. Creates a new file or overwrites an existing one. |
| `a`  | Append mode. Adds data to the end of an existing file. |
| `r+` | Read and write mode. File must exist. |
| `w+` | Write and read mode. Overwrites the file. |
| `a+` | Append and read mode. Creates the file if it doesn’t exist. |

## Best Practices for File Handling
- Always close files after reading/writing using `with open()` to prevent memory leaks.
- Use exception handling (`try-except`) to handle file-related errors gracefully.
- Avoid overwriting critical files accidentally by checking if they exist before writing.
- Use logging instead of print statements for better debugging and monitoring.

File handling is a crucial skill in Python, making it easy to work with different types of files efficiently. 🚀

