# Tracker API (0.3.0)

A FastAPI-based project for project management.  

## Getting started (First launch)

### 1. Create a virtual environment

```bash
# Linux / macOS:

python3 -m venv venv
source venv/bin/activate
```

```powershell
# Windows (PowerShell):

python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies and local package

```bash
pip install -r requirements.txt
pip install -e .
```

This installs all Python dependencies and your local package in editable mode, so any changes in the code are immediately available.

### 3. Configure environment variables

Before starting the server, create a `.env` file in the root directory and add the following variables:

```bash
MONGODB_APPNAME = example     # Your app name
MONGODB_DBNAME = example      # Your database name
MONGODB_USERNAME = example    # Your username
MONGODB_PASSWORD = example    # Your password
```


### 4. Start the server

```bash
uvicorn app.main:app --reload
```

If using the default host and port, the server will be available at: http://127.0.0.1:8000  
API documentation: http://127.0.0.1:8000/docs

## Next launches

### 1. Activate the virtual environment

```bash
# Linux / macOS:

source venv/bin/activate
```

```powershell
# Windows (PowerShell):

venv\Scripts\activate
```

## 2. Start the server

```bash
uvicorn app.main:app --reload
```