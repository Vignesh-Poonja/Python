import os

# Load environment variables from .env
load_dotenv()

# Access environment variables
print(os.getenv("User_Id"))
print(os.getenv("password"))
