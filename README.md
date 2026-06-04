
# Python-Assignments
A collection of Python assignments and practice programs covering core concepts, problem-solving, and hands-on exercises. This repository tracks my continuous learning and improvement in Python programming.
=======
# 🔐 Python Password Manager

A secure command-line password manager built with Python that uses **Fernet symmetric encryption** to store and retrieve passwords safely.

---

## 📋 Features

- 🔑 Master password protection via `.env` file
- 🔒 Fernet (AES-128) encryption for all stored passwords
- 📁 Passwords saved persistently in a local text file
- ➕ Add new credentials
- 👁️ View decrypted credentials on demand
- 🚪 Simple quit option

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| `cryptography` | Fernet encryption |
| `python-dotenv` | Load master password from `.env` |
| `os` | Environment variable access |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/sidsakhare/Python-Assignments.git
cd Python-Assignments
```

### 2. Install Dependencies
```bash
pip install cryptography python-dotenv
```

### 3. Create `.env` File
Create a `.env` file in the project directory:
```
Master_pwd=your_master_password_here
```
> ⚠️ Never share or commit this file!

### 4. Generate Encryption Key
Run this **once** before first use — add temporarily to `pass.py`:
```python
write_key()
```
This creates a `key.key` file. Remove the line after running.

### 5. Run the App
```bash
python pass.py
```

---

## 💻 Usage

```
what is the master password: ****

would you like to add a new password or view existing ones (add, view) or quit q=
```

| Command | Action |
|---------|--------|
| `add` | Add a new username & password |
| `view` | View all saved passwords (decrypted) |
| `q` | Quit the application |

---

## 📁 Project Structure

```
📦 Project Folder
 ┣ 📄 pass.py          # Main application
 ┣ 🔑 key.key          # Encryption key (DO NOT SHARE)
 ┣ 🔒 .env             # Master password (DO NOT SHARE)
 ┣ 📄 password.txt     # Encrypted passwords storage
 ┗ 📄 .gitignore       # Protects secret files
```

---

## 🔒 Security Notes

> ⚠️ This is a learning project. For production use, consider a dedicated password manager.

- `.env`, `key.key`, and `password.txt` are listed in `.gitignore` and **never pushed to GitHub**
- Losing `key.key` means **all stored passwords become unrecoverable**
- Keep backups of `key.key` in a secure location

---

## 📚 Concepts Learned

- Symmetric encryption with `cryptography.fernet`
- Environment variable management with `python-dotenv`
- File I/O in Python
- Basic CLI application design
- Git secret management with `.gitignore`

---

## 👤 Author

**Sid Sakhare**  
GitHub: [@sidsakhare](https://github.com/sidsakhare)

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).


