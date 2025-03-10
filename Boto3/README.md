
---

### **Boto3**
```md
# Boto3 - AWS SDK for Python

## Introduction
Boto3 is the Amazon Web Services (AWS) SDK for Python, which allows Python developers to interact with AWS services programmatically.

## Installation
To install Boto3, use pip:
```bash
pip install boto3
```

## Configuration
Before using Boto3, configure AWS credentials using the AWS CLI:
```bash
aws configure
```
You will be prompted to enter:
- **AWS Access Key ID**
- **AWS Secret Access Key**
- **Default region name**
- **Default output format (optional)**

## Usage
### Listing S3 Buckets
```python
import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()

for bucket in response['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')
```

### Uploading a File to S3
```python
s3.upload_file("localfile.txt", "my-bucket-name", "s3-object-key.txt")
```

### Common Use Cases
- Managing **EC2** instances
- Uploading/downloading files to/from **S3**
- Managing **DynamoDB** tables
- Working with **IAM roles and policies**
- Automating **Lambda** function deployments

## Documentation
For detailed documentation, visit: [Boto3 Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

---

### **Flask**
```md
# Flask - Python Web Framework

## Introduction
Flask is a lightweight and powerful web framework for Python, designed for building web applications and APIs.

## Installation
To install Flask, use pip:
```bash
pip install flask
```

## Creating a Simple Flask App
Create a file named `app.py`:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

Run the application:
```bash
python app.py
```
Then open `http://127.0.0.1:5000/` in your browser.

## Routing Example
```python
@app.route('/about')
def about():
    return "This is the About Page"
```

## Handling JSON Requests
```python
from flask import request, jsonify

@app.route('/api/data', methods=['POST'])
def get_data():
    data = request.get_json()
    return jsonify({"message": "Data received", "data": data})
```

## Common Use Cases
- Building **REST APIs**
- Developing **microservices**
- Creating **web applications**
- Handling **form submissions** and **database connections**

## Documentation
For detailed documentation, visit: [Flask Docs](https://flask.palletsprojects.com/)

---
