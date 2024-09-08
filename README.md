# SaintTodo

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Django](https://img.shields.io/badge/Django-4.0+-brightgreen.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-yellow.svg)](https://www.python.org/)

## Introduction

**SaintTodo** is a simple and efficient To-Do List application built using the [Django](https://www.djangoproject.com/) web framework. This app allows users to manage their daily tasks by adding, updating, and deleting items from their personal to-do lists.

Visit the repository here: [SaintTodo on GitHub](https://github.com/SaintNong/SaintTodo)

## Features

- **Task Management:** Add, update, and delete tasks from your to-do list.
- **Task Completion:** Mark tasks as completed.
- **User Authentication:** Register and log in to maintain a personal task list.
- **Design:** It was designed.
- **Sort of decent UI:** Simple and intuitive interface for task management.

## Tech Stack

- **Framework:** Django
- **Language:** Python
- **Database:** SQLite
- **Frontend:** HTML, CSS (Bulma.css), JavaScript (anime.js, jquery)

## Installation

Follow the steps below to set up and run SaintTodo on your local machine.

### Prerequisites

- Python 3 installed on your machine.
- Git installed.

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/SaintNong/SaintTodo.git
   cd SaintTodo
   ```
2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Complete migrations
```bash
python manage.py migrate
```

5. Run the server and visit http://127.0.0.1:8000/ to see the app!
```bash
python manage.py runserver
```
## License

This project is licensed under the MIT License - see the LICENSE file for details.

