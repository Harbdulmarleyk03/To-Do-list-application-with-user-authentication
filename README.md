# To-Do List Application with User Authentication

A full-featured to-do list web application built with Django that allows users to manage their tasks with complete user authentication and CRUD functionality.

## Features

- **User Authentication**
  - User registration
  - User login/logout
  - Secure password handling
  - Session management

- **Task Management**
  - Create new tasks
  - View all tasks
  - Update/edit existing tasks
  - Delete tasks
  - Mark tasks as complete/incomplete

- **Search Functionality**
  - Search through your task list
  - Filter tasks based on keywords

- **User-Specific Data**
  - Each user has their own private task list
  - Tasks are isolated per user account

## Technologies Used

- **Backend:** Django (Python)
- **Database:** SQLite (default) / PostgreSQL
- **Frontend:** HTML, CSS, JavaScript
- **Authentication:** Django's built-in authentication system

## Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- virtualenv (recommended)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Harbdulmarleyk03/To-Do-list-application-with-user-authentication.git
cd To-Do-list-application-with-user-authentication
```

### 2. Create a Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install Django:

```bash
pip install django
```

### 4. Apply Database Migrations

```bash
cd todolist
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account for accessing the Django admin panel.

### 6. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

### Registration and Login

1. Navigate to the registration page to create a new account
2. After registration, log in with your credentials
3. You'll be redirected to your personal task dashboard

### Managing Tasks

- **Create a Task:** Click on "Add Task" or the create button and fill in the task details
- **View Tasks:** All your tasks are displayed on the main dashboard
- **Edit a Task:** Click on the edit icon next to any task to modify it
- **Delete a Task:** Click on the delete icon to remove a task
- **Complete a Task:** Mark tasks as complete by checking the checkbox or clicking the complete button
- **Search Tasks:** Use the search bar to find specific tasks

## Project Structure

```
To-Do-list-application-with-user-authentication/
│
├── todolist/                 # Main Django project directory
│   ├── todolist/            # Project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── tasks/               # Tasks app (likely name)
│   │   ├── models.py        # Database models
│   │   ├── views.py         # View functions
│   │   ├── urls.py          # URL routing
│   │   ├── forms.py         # Form definitions
│   │   └── templates/       # HTML templates
│   │
│   ├── manage.py            # Django management script
│   └── db.sqlite3           # SQLite database
│
└── README.md                # This file
```

## API Endpoints (if applicable)

If your application includes REST API endpoints:

- `POST /api/register/` - User registration
- `POST /api/login/` - User login
- `GET /api/tasks/` - Get all tasks
- `POST /api/tasks/` - Create a new task
- `PUT /api/tasks/<id>/` - Update a task
- `DELETE /api/tasks/<id>/` - Delete a task

## Database Schema

### User Model
- Uses Django's default User model with username, email, and password

### Task Model (Example)
- `id` - Primary key
- `user` - Foreign key to User
- `title` - Task title
- `description` - Task description
- `completed` - Boolean status
- `created_at` - Timestamp
- `updated_at` - Timestamp

## Security Features

- CSRF protection enabled
- Password hashing using Django's built-in system
- User session management
- Login required decorators for protected views
- SQL injection prevention through Django ORM

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Open a Pull Request

## Known Issues

- Add any known bugs or limitations here

## Future Enhancements

- [ ] Add task categories/tags
- [ ] Implement task priority levels
- [ ] Add due dates and reminders
- [ ] Email notifications
- [ ] Dark mode toggle
- [ ] Mobile responsive design improvements
- [ ] Task sharing between users
- [ ] Export tasks to PDF/CSV

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions or support, please open an issue on GitHub or contact the repository owner.

## Acknowledgments

- Django documentation and community
- Contributors and testers

---

**Note:** Make sure to keep your dependencies updated and follow Django security best practices when deploying to production.
