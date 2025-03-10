# Python Workspace Setup

This guide provides step-by-step instructions to create and manage a Python workspace using a virtual environment.

## 1. Creating a Python Workspace

To set up a new Python virtual environment, run the following command:

```powershell
python -m venv project-abc\venv
```

## 2. Activating the Virtual Environment

To activate the virtual environment in PowerShell:

```powershell
.\project-abc\venv\Scripts\Activate.ps1
```

If you encounter execution policy issues, you may need to run:

```powershell
Set-ExecutionPolicy Unrestricted -Scope Process
```

Then, retry activating the environment.

## 3. Installing Packages

Once the virtual environment is activated, install necessary packages using:

```powershell
pip install numpy pandas
```

To install packages from a `requirements.txt` file:

```powershell
pip install -r requirements.txt
```

## 4. Deactivating the Virtual Environment

To deactivate the virtual environment, use:

```powershell
deactivate
```

## 5. Deleting the Virtual Environment

To delete the virtual environment along with all dependencies, run:

```powershell
Remove-Item -Recurse -Force project-abc
```

## 6. Additional Commands

- To check installed packages:
  ```powershell
  pip list
  ```
- To create a `requirements.txt` file for future installations:
  ```powershell
  pip freeze > requirements.txt
  ```
- To check Python version:
  ```powershell
  python --version
  ```

## 7. Notes

- Always activate the virtual environment before running Python scripts.
- Use a virtual environment to avoid conflicts with system-wide Python packages.
- It is recommended to use `requirements.txt` for dependency management.

Happy Coding! 🚀

## 8. Importance of a Python Workspace

Setting up a dedicated Python workspace with a virtual environment is crucial for maintaining clean, isolated environments for different projects. It ensures that dependencies are managed effectively, preventing conflicts with system-wide packages. Using virtual environments also makes it easier to collaborate with others by sharing exact package requirements. Additionally, having a well-organized workspace improves productivity by keeping all project files and configurations structured and easily accessible.

