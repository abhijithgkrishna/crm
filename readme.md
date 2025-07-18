
---

# Django CRM

A simple Customer Relationship Management (CRM) web application built with Django. This project provides user authentication (login, logout, registration) and basic CRUD for customer records, using a MySQL database. The UI uses Bootstrap for a clean and responsive design.

## Features

- User registration, login, and logout (with flash messages)
- View all customer records (home page)
- Add, update, delete, and view individual records (CRUD)
- Responsive Bootstrap-based interface
- MySQL database integration

## Project Structure

```
crm/
├── crm/                  # Django project settings, URLs, WSGI/ASGI
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── website/              # Main Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── models.py
│   ├── templates/
│   │   ├── add_record.html
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── navbar.html
│   │   ├── record.html
│   │   ├── register.html
│   │   └── update_record.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── mydb.py               # Script to create the MySQL database
├── manage.py             # Django management script
└── readme.md             # Project documentation
```

## Setup Instructions

### Prerequisites

- Python 3.x
- Django (version 5.2 or compatible)
- MySQL server
- `mysql-connector-python` (for the database creation script)

### 1. Clone the Repository

```bash
git clone https://github.com/abhijithgkrishna/crm
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

## Available Routes

- `/` : Home page (login form and list of records)
- `/register` : User registration
- `/logout` : Log out
- `/record/<int:pk>` : View a single record (login required)
- `/add_record` : Add a new record (login required)
- `/update_record/<int:pk>` : Update a record (login required)
- `/delete_record/<int:pk>` : Delete a record (login required)

## Usage

- **Home Page:** Login form for existing users and a list of all records.
- **Register:** Create a new user account.
- **Logout:** Log out of the application.
- **Add/Update/Delete/View Record:** Manage customer records (requires login).

Navigation is available via the top navbar.

## Customization

- Add your own CRM models in `website/models.py`.
- Extend views and templates to add CRM features (contacts, leads, etc.).
- Adjust forms in `website/forms.py` for custom fields.

## Security Notes

- The default database credentials are for development only. Change them for production.
- The Django `SECRET_KEY` in settings is for development. Generate a new one for production.
- Set `DEBUG = False` and configure `ALLOWED_HOSTS` before deploying.
- Use strong, unique passwords for all accounts.
