# Command Line Arguments


************************************************************************************************
# Env Variables
sensitive Information

Using .env Files (Recommended for Projects)

Instead of setting environment variables manually, you can store them in a .env file and load them using python-dotenv.

# Step 1: Install dotenv
pip install python-dotenv

# Step 2: Create a .env File
Create a file .env in your project directory:

MY_ENV_VAR=Hello, World!
SECRET_KEY=12345

# Step 3: Load the .env File in Python
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Access environment variables
print(os.getenv("MY_ENV_VAR"))  # Output: Hello, World!
print(os.getenv("SECRET_KEY"))  # Output: 12345