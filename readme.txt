# 🧢 Crowd-Funding Console App (Python)

A simple Python console application to simulate a crowdfunding platform. Users can register, log in, create fundraising projects, manage them, and donate to others — all via the terminal.

---

## 🚀 Features

### 👤 User Authentication
- ✅ Registration with:
  - First name, last name
  - Valid Egyptian phone number
  - Email and password (with confirmation)
- ✅ Login using email and password

### 📦 Project Management
- ✅ Create projects with:
  - Title, description
  - Target amount
  - Start and end dates (validated)
  - Category (e.g. Health, Education)
- ✅ View all projects
- ✅ Edit or delete **only your own** projects
- ✅ Search projects by **start date**
- ✅ Donate to any project (tracked per project)

### 💾 Data Storage
- Uses **JSON files**:
  - `users.json` → Stores registered users
  - `projects.json` → Stores all project data

---

## 📁 Project Structure

```bash
crowdfunding_app/
├── main.py            # App entry point
├── auth.py            # Handles user registration and login
├── project.py         # Project creation, editing, donations
├── utils.py           # Shared helpers: validation, file I/O
├── data/
│   ├── users.json     # User accounts
│   └── projects.json  # Project campaigns

****=== Created by Ahmed Salem ===****