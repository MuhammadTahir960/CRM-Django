<h1 align="center">🗂️ Django CRM</h1>

<p align="center">
  A full-featured <strong>Customer Relationship Management</strong> web app built with Django &amp; MySQL.
  <br/>
  Manage your customer records with ease — add, view, update, and delete, all behind secure authentication.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Django-6.0.2-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [Security](#-security)
- [License](#-license)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 **Authentication** | Register, log in, and log out using Django's built-in auth system |
| 🏠 **Dashboard** | View all customer records at a glance in a clean table |
| ➕ **Add Records** | Create new customer entries via a validated form |
| 👁️ **View Records** | Inspect the full details of any individual customer |
| ✏️ **Update Records** | Edit existing customer information in real time |
| 🗑️ **Delete Records** | Remove entries with a single click |
| 🛡️ **Route Protection** | Unauthenticated users are automatically redirected to login |
| 💬 **Flash Messages** | Bootstrap-styled success & error feedback on every action |
| 🌍 **Env-Based Config** | All secrets and DB credentials managed via a `.env` file |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.10+, Django 6.0.2 |
| **Database** | MySQL |
| **Frontend** | HTML5, Bootstrap 5 |
| **Templating** | Django Template Language |
| **Configuration** | Environment Variables (`.env`) |

---

## 📁 Project Structure

```
Django-CRM/
├── CRM/                            # Django project root
│   ├── CRM/                        # Core project configuration
│   │   ├── settings.py             # Settings — loaded from environment variables
│   │   ├── urls.py                 # Root URL configuration
│   │   ├── wsgi.py                 # WSGI entry point
│   │   └── asgi.py                 # ASGI entry point
│   │
│   ├── Website/                    # Main CRM application
│   │   ├── migrations/             # Database migration files
│   │   ├── templates/              # HTML templates
│   │   │   ├── base.html           # Base layout (shared across all pages)
│   │   │   ├── navbar.html         # Navigation bar partial
│   │   │   ├── login.html          # Login page
│   │   │   ├── register.html       # User registration page
│   │   │   ├── home.html           # Dashboard — all records
│   │   │   ├── record.html         # Individual record detail view
│   │   │   ├── add_record.html     # Add new record form
│   │   │   └── update_record.html  # Edit existing record form
│   │   ├── models.py               # Record data model
│   │   ├── forms.py                # SignUpForm & AddRecordForm
│   │   ├── views.py                # View functions (CRUD + auth logic)
│   │   ├── urls.py                 # App-level URL patterns
│   │   ├── apps.py                 # App configuration
│   │   ├── tests.py                # App-level tests
│   │   └── admin.py                # Django admin configuration
│   │
│   ├── requirements.txt            # Python dependencies list
│   ├── .env.example                # Template for required environment variables
│   ├── .gitignore                  # Git ignore rules
│   ├── manage.py                   # Django management CLI
│   ├── LICENSE                     # Project license
│   └── README.md                   # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- [Python 3.10+](https://www.python.org/downloads/)
- [MySQL Server](https://dev.mysql.com/downloads/mysql/)
- `pip` (comes with Python)

---

### 1. Clone the Repository

```bash
git clone https://github.com/MuhammadTahir960/Django-CRM.git
cd Django-CRM
```

### 2. Create & Activate a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r CRM/requirements.txt
```

### 4. Create the MySQL Database

Log into MySQL and run:

```sql
CREATE DATABASE your_db_name;
```

### 5. Configure Environment Variables

Copy the example file and fill in your own values:

```bash
cp CRM/.env.example CRM/.env
```

Open `CRM/.env` and update it:

```env
SECRET_KEY=your_secret_key_here
DEBUG=True

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
```

> 💡 Generate a strong secret key with:
> ```bash
> python -c "import secrets; print(secrets.token_urlsafe(50))"
> ```

### 6. Apply Database Migrations

```bash
cd CRM
python manage.py migrate
```

### 7. Create an Admin Superuser *(Optional)*

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Visit the app at **[http://127.0.0.1:8000](http://127.0.0.1:8000)** 🎉

---

## 🌍 Environment Variables

All sensitive configuration is loaded from environment variables. Use `.env.example` as a reference:

| Variable | Required | Default | Description |
|---|---|---|---|
| `SECRET_KEY` | ✅ Yes | `mydevsecretkey...` | Django cryptographic secret key |
| `DEBUG` | ❌ No | `False` | Set to `True` in development only |
| `DB_NAME` | ✅ Yes | — | MySQL database name |
| `DB_USER` | ✅ Yes | — | MySQL username |
| `DB_PASSWORD` | ✅ Yes | — | MySQL password |
| `DB_HOST` | ❌ No | `localhost` | MySQL host |
| `DB_PORT` | ❌ No | `3306` | MySQL port |

---

## 🔒 Security

- All record views require authentication — unauthenticated users are redirected to `/login/`
- Passwords are hashed using Django's default **PBKDF2** algorithm
- **CSRF protection** is enabled on all forms
- Secrets are never hardcoded — all sensitive values live in `.env` (excluded from Git)
- Set `DEBUG=False` and use a strong `SECRET_KEY` before deploying to production

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute for any purpose.

---

<p align="center">
  Built with ❤️ using <a href="https://www.djangoproject.com/">Django</a>
</p>
