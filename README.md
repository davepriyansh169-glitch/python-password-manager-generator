# Python Password Manager and Password Generator

A beginner-friendly Python project that combines a password generator with a local password manager. It includes both a command-line workflow and a Streamlit-based interface for generating passwords and storing credentials with encryption.

## Features

- Generate passwords with configurable length
- Optionally include numbers and special characters
- Store credentials locally in an encrypted format
- Unlock stored credentials with a master password
- Use either the command-line scripts or the Streamlit app

## Encryption and Security Overview

- Uses `cryptography` with `Fernet` for symmetric encryption
- Uses `hashlib` for master password hashing
- Uses `base64` and PBKDF2-based key derivation in the project
- Password data is intended to stay on the local machine
- Sensitive runtime files such as saved passwords, key files, and local master-password files should not be committed to GitHub

## Tech Stack

- Python
- Streamlit
- cryptography
- hashlib
- base64
- os

## Project Structure

```text
.
+-- app_security.py
+-- pass_generate.py
+-- pass_manage.py
+-- requirements.txt
+-- README.md
```

Local runtime files such as `passwords.txt`, `master.pass`, and `key.key` are intentionally excluded from GitHub with `.gitignore`.

## Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Streamlit App

```bash
streamlit run app_security.py
```

## Usage

### Password Generator

- Open the Streamlit app or run the CLI generator script
- Choose the desired password options
- Generate a password for personal local use

CLI option:

```bash
python pass_generate.py
```

### Password Manager

- Open the Streamlit app or run the CLI manager script
- Enter a master password
- Add or view stored credentials locally

CLI option:

```bash
python pass_manage.py
```

## Disclaimer

This project is intended for educational, learning, and local-use purposes. It is not a production-ready password manager and should not be treated as a replacement for a professionally audited security product.

## Future Improvements

- Improve input validation and error handling
- Add search, edit, and delete options for saved credentials
- Add stronger file-structure separation for the app and CLI tools
- Add unit tests
- Add export/import controls with safer workflows
- Improve UI polish and user guidance
