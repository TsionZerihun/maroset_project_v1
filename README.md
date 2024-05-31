# Maroset Project v1

Welcome to the Maroset Project v1 repository! This project is designed to [provide a brief description of the project's purpose and functionality].

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Contact](#contact)

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TsionZerihun/maroset_project_v1.git
   cd maroset_project_v1
2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install dependencies**:
   ```bash
   python manage.py runserver

## Usage

To start the project, run:


1. **Clone the repository**:
   ```bash
   git clone https://github.com/TsionZerihun/maroset_project_v1.git
   cd maroset_project_v1
2. Navigate to http://127.0.0.1:8000/ in your browser to view the project.

3. Example usage
   ```python
   #To create a superuser for accessing the admin panel, run:
   python manage.py createsuperuser
   ```

   ```python
   #Ensure the database schema is up-to-date with the latest changes by running:
   python manage.py makemigrations
   python manage.py migrate
   ```

   ```python
   #To collect all static files in a single location, run:
   python manage.py collectstatic
   ```


## Features

User Authentication: Secure login and registration system.

1. **User Authentication: Secure login and registration system.**:
2. **Dashboard: Interactive dashboard for users to post jobs, create profiles, apply for jobs, and chat with job owners their activities.**:
3. **Dashboard: Interactive dashboard for admin to approve job, Block users, with job owners, and receive notification.**:

## Folder Structure

```bash
maroset_project_v1/
├── assets/
├── company/
├── dashboard/
├── media/
├── resume/
├── static/
├── templates/
├── users/
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TsionZerihun/maroset_project_v1.git
   cd maroset_project_v1
2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

#### If you have any questions or feedback, feel free to contact me:

- Email: tsionzelekezerihun@gmail.com
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/tsion-zeleke/)
- GitHub: [TsionZerihun](https://github.com/TsionZerihun)
