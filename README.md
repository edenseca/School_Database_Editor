# C++ School Database Editor

**Authors: Nick Ek Ethan Secakusuma**

## Overview
This C++ Database Management Program provides functionality for importing and managing data related to users, students, teachers, and administrators. It leverages SQLite3 for database management and allows users to perform various operations based on their roles.

## Features
- **Importing Data:**
  - Import user, student, teacher, and administrator data from SQLite3 database tables.
- **User Authentication:**
  - Implement a login system for users, ensuring secure access to the system based on user credentials.
- **Role-Based Operations:**
  - Students can perform actions like viewing schedules, adding or dropping courses, and searching for courses.
  - Instructors can view schedules, print class lists, and search for courses.
  - Administrators can add or remove entries from the database, search or print student/course information, and manage courses.
- **Database Operations:**
  - Interact with SQLite3 databases to perform CRUD (Create, Read, Update, Delete) operations on user, student, teacher, and administrator data.

## Technologies Used
- **Language:** C++
- **Database Management:** SQLite3

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/edenseca/School_Database_Editor.git
   
2. Navigate to the project directory:
   ```bash
   cd <project directory>

3. Compile the program:
   ```bash
    g++ -o main main.cpp -lsqlite3

5. Run the compiled executable:
    ```bash
    ./main



