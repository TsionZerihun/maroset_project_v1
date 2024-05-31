# Maroset Project v1

Welcome to the Maroset Project v1 repository! This Project is designed to serve as a comprehensive platform for job seekers and employers. By providing features for job postings, applications, and administrative oversight, it aims to simplify the job search and hiring process. The platform ensures that users can easily create and manage job postings, apply for jobs, and report issues, while administrators can effectively manage and moderate the content.

# Maroset Project v1: Key Functionalities

## User Registration and Authentication
- **Register**: Create a new user account.
- **Login**: Access an existing user account.
- **Logout**: Sign out of the user account.
  
![image](https://github.com/TsionZerihun/maroset_project_v1/assets/101357449/83e16a5d-1cc1-47d4-ac59-6fbd4e4abf59)


## User Profile Management
- **View Profile**: Display user profile details.
- **Update Profile**: Edit and update user profile information.
  
![image](https://github.com/TsionZerihun/maroset_project_v1/assets/101357449/6762807f-f5ff-49c7-9cfc-b1b2fdb2f7b3)


## Job Postings Management
- **Create Job Posting**: Add new job listings.
- **Update Job Posting**: Edit existing job listings.
- **Admin Update Job Posting**: Administrators can edit any job listings.

![image](https://github.com/TsionZerihun/maroset_project_v1/assets/101357449/3527f3c9-3ffc-4b16-833a-23506646bda8)


## Job Applications
- **Apply to Job**: Submit applications for job postings.
- **View All Applicants**: Job owners can view applicants for their job postings.

## Job Reporting
- **Report Job Posting**: Flag job postings for review.
- **View Report Reasons**: Admins can view reasons for reported jobs.
- **About Reported Job**: Admins can access detailed information on reported jobs.
  ![image](https://github.com/TsionZerihun/maroset_project_v1/assets/101357449/3b5249ff-df57-45f2-a4b2-d05e1ff38937)


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
