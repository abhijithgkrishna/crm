
---

# Django CRM

A simple Customer Relationship Management (CRM) web application built with Django. This project provides basic user authentication (login, logout, registration) and is set up to use a MySQL database. The UI uses Bootstrap for a clean and responsive design.

## Features

- User registration with username, email, first name, last name, and password
- User login and logout
- Flash messages for authentication feedback
- Responsive Bootstrap-based interface
- MySQL database integration

## Project Structure

```
<code_block_to_apply_changes_from>
```

## Setup Instructions

### Prerequisites

- Python 3.x
- Django (version 5.2 or compatible)
- MySQL server
- `mysql-connector-python` (for the database creation script)

### 1. Clone the Repository

```bash
git clone <repository-url>
cd CRM/crm
```

### 2. Create the MySQL Database

Edit `mydb.py` if you need to change the database credentials. Then run:

```bash
python mydb.py
```

This will create a database named `crm_db` with user `root` and password `test1234` (default settings).

### 3. Install Python Dependencies

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install django mysql-connector-python
```

### 4. Configure Django Settings

Check `crm/settings.py` for database credentials and other settings. Adjust as needed for your environment.

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

Visit [http://localhost:8000/](http://localhost:8000/) in your browser.

## Usage

- **Home Page:** Login form for existing users.
- **Register:** Create a new user account.
- **Logout:** Log out of the application.

Navigation is available via the top navbar.

## Customization

- Add your own CRM models in `website/models.py`.
- Extend views and templates to add CRM features (contacts, leads, etc.).

## Security Notes

- The default database credentials are for development only. Change them for production.
- The Django `SECRET_KEY` in settings is for development. Generate a new one for production.
- Set `DEBUG = False` and configure `ALLOWED_HOSTS` before deploying.
