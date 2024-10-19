# University Management System

## Student Info:

**Name** : Umer Ali
**Batch** : 65
**Roll No**: PIAIC243523
**Course** : Certified Cloud Native Generative AI

## Project Overview

This project is a Python-based **University Management System** designed to manage various university operations such as human resources, assets, departments, library, courses, and hostel management. The project was developed as part of the **Certified Cloud Native Generative AI** course (Batch 65) offered by **PIAIC**.

## Project Structure

The system consists of various classes, each responsible for handling specific aspects of the university. Below is a breakdown of the core components:

### Classes

1. **University**: 
   - Base class holding the university's name and location.
   
2. **Human (Inherits University)**:
   - Manages university human resources, including students, teachers, librarians, and labors.
   
3. **Assets (Inherits University)**:
   - Manages physical university assets such as buses, rooms, air conditioners (AC), and computers.
   
4. **Campus (Inherits University)**:
   - Handles the different university campuses.
   
5. **Department (Inherits Campus)**:
   - Manages the departments within the university.
   
6. **Library (Inherits Department)**:
   - Manages the university's library, including books and categories.
   
7. **Course (Inherits Department)**:
   - Handles the different courses offered by the university.
   
8. **Hostel (Inherits University)**:
   - Manages student hostels and the list of students residing in them.
   
9. **Student (Inherits Course)**:
   - Manages individual student information such as name, roll number, subject, and assigned teacher.
   
10. **Teacher (Inherits Course)**:
    - Manages individual teacher information such as name, number, subject, and the classes they teach.

## Features

- **Human Resource Management**: Add/remove university staff and students.
- **Asset Management**: Track university buses, rooms, air conditioners, and computers.
- **Campus & Department Management**: Manage multiple campuses and departments.
- **Library Management**: Add books and categories to the university library.
- **Course Management**: Add and manage courses offered by the university.
- **Hostel Management**: Track students residing in hostels.
- **Student & Teacher Profiles**: Display detailed information about individual students and teachers.

## How to Run

1. Clone the repository to your local machine.
2. Install Python 3.x if you haven't already.
3. Run the main Python file (`main.py` or equivalent) in your Python environment.

```bash
python main.py
