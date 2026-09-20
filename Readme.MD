# Calculator MCP Server

This project contains a small Python Model Context Protocol (MCP) server with a calculator tool and a greeting resource.

## Project purpose

- Adds a calculator tool with operations: `+`, `-`, `*`, `/`
- Validates divide-by-zero errors
- Exposes a greeting resource for named values
- Can be used with the configured VS Code MCP server setup

## Prerequisites

Before running the project, make sure you have:

- Python 3.10 or newer
- PowerShell or Command Prompt on Windows
- Access to the project folder

## Setup

1. Open a terminal in the project folder:

   ```powershell
   cd "C:\Users\ad\projects\webscrapping-python\my_python_project"
   ```

2. Create a virtual environment:

   ```powershell
   python -m venv venv
   ```

3. Activate the virtual environment:

   In PowerShell:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   In Command Prompt:

   ```cmd
   .\venv\Scripts\activate.bat
   ```

4. Upgrade pip and install dependencies:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Execution

Run the MCP server directly:

```powershell
python calculator.py
```

Or explicitly use the virtual environment interpreter:

```powershell
.\venv\Scripts\python.exe calculator.py
```

The server is configured in `.vscode/mcp.json` to run with the virtual environment Python interpreter.

## Validation

After setup, validate the calculator logic with a Python command:

```powershell
python -c "import calculator; print('RESULT1=', calculator.calculate(2, '+', 3)); print('RESULT2=', calculator.calculate(9, '/', 3)); print('OK')"
```

Expected output:

```text
RESULT1= 5
RESULT2= 3.0
OK
```

You can also validate error handling:

```powershell
python -c "import calculator; print(calculator.calculate(10, '/', 0))"
```

This should raise a `ValueError` with the message:

```text
Cannot divide by zero
```

## Useful checks

Check the project files:

```powershell
dir
```

Check Python version:

```powershell
python --version
```

## Notes

- The project uses the official MCP Python SDK.
- The server entry point is `calculator.py`.
- The dependency list is stored in `requirements.txt`.
