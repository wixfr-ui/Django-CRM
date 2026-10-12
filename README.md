# Django CRM

A Customer Relationship Management (CRM) application built with Python, Django, and MySQL.

## Requirements

- Python
- MySQL Server (if using the MySQL configuration)
- pip

## Installation

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Create a virtual environment:

   `python -m venv .venv`

4. Activate the environment on Windows:

   `.venv\Scripts\Activate.ps1`

5. Install dependencies:

   `python -m pip install -r requirements.txt`

6. Configure your database credentials using the project's configuration instructions.
7. Apply database migrations:

   `python manage.py migrate`

8. Start the development server:

   `python manage.py runserver`

9. Open `http://127.0.0.1:8000/` in your browser.
