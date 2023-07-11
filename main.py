import sqlite3

from User import *
from Student import *
from Teacher import *
from Admin import *


con = sqlite3.connect('assignment3.db')
cur = con.cursor()

admin_database = []
teacher_database = []
student_database = []
def get_student_data():

    # Select all rows from the 'user' table
    select_query = 'SELECT * FROM STUDENT'
    cur.execute(select_query)
    rows = cur.fetchall()
    print('Importing Student database...')
    # Iterate through the rows and create User objects
    for row in rows:
        id = row[0]
        first_name = row[1]
        last_name = row[2]
        email = row[3]
        grad_year = row[4]
        major = row[5]
        student = Student(id, first_name, last_name, email, grad_year, major, 0)
        student_database.append(student)
    print('Student Database import successful!')


def get_teacher_data():

    # Select all rows from the 'user' table
    select_query = 'SELECT * FROM INSTRUCTOR'
    cur.execute(select_query)
    rows = cur.fetchall()
    print('Importing Teacher database...')
    # Iterate through the rows and create User objects
    for row in rows:
        id = row[0]
        first_name = row[1]
        last_name = row[2]
        title = row[3]
        hire_year = row[4]
        dept = row[5]
        email = row[6]
        teacher = Teacher(id, first_name, last_name, title, hire_year, dept, email)
        teacher_database.append(teacher)
    print('Teacher Database import successful!')


def get_admin_data():

    # Select all rows from the 'user' table
    select_query = 'SELECT * FROM ADMIN'
    cur.execute(select_query)
    rows = cur.fetchall()
    print('Importing Admin database...')
    # Iterate through the rows and create User objects
    for row in rows:
        id = row[0]
        first_name = row[1]
        last_name = row[2]
        title = row[3]
        office= row[4]
        email = row[5]
        admin = Admin(id, first_name, last_name, title, office, email)
        admin_database.append(admin)
    print('Admin Database import successful!')


def create_course_table():
    cur.execute("""
        INSERT INTO course VALUES
            ('40001', 'Physics', 'BSAS', '8-920', 'MWF', 'Fall', '2024', '4' ),
            ('40002', 'Physics 2', 'BSCO', '2-320', 'TTR', 'Spring', '2024', '4' ),
            ('40003', 'Calculus', 'BCOS', '8-920', 'MWF', 'Fall', '2024', '4' ),
            ('40004', 'Calculus 2', 'BSEE', '10-1120', 'MWF', 'Spring', '2024', '4' ),
            ('40005', 'Psychology', 'HUSS', '10-12', 'TTR', 'Fall', '2024', '2' )
    """)
    con.commit()


def display_student():      # Teachers
    cur.execute("SELECT * FROM student")
    t = cur.fetchall()

    print("STUDENTS:")
    for row in t:
        print(row)


def display_teachers():     # Teacher/Admin
    cur.execute("SELECT * FROM instructor")
    x = cur.fetchall()

    print("TEACHERS:")
    for row in x:
        print(row)


def display_admin():        # Admin
    cur.execute("SELECT * FROM admin")
    y = cur.fetchall()

    print("ADMINS:")
    for row in y:
        print(row)


def display_courses():      # Everyone
    cur.execute("SELECT * FROM course")
    z = cur.fetchall()

    print("COURSES:")
    for row in z:
        print(row)


def display_all_table():    # Not needed
    display_student()
    display_teachers()
    display_admin()
    display_courses()


def student_insert():       # Admin
    wid = int(input("Enter students WID: "))
    first_name = input("Enter students first name: ")
    last_name = input("Enter students last name: ")
    grad_year = int(input("Enter students expected graduation year: "))
    major = input("Enter students major: ")
    email = input("Enter student email without @domain: ")
    cur.execute("INSERT INTO student VALUES ('{}','{}','{}','{}','{}','{}')".format(wid, first_name, last_name, grad_year,   major, email))
    con.commit()


def teacher_insert():       # Admin
    wid = int(input("Enter teachers WID: "))
    first_name = input("Enter teachers first name: ")
    last_name = input("Enter teachers last name: ")
    title = input("Enter title of instructor: ")
    year_hired = int(input("Enter teachers year of hire: "))
    department = input("Enter teachers department: ")
    email = input("Enter student email without @domain: ")
    cur.execute("INSERT INTO instructor VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(wid, first_name, last_name, title, year_hired, department, email))
    con.commit()


def admin_insert():         # Admin
    wid = int(input("Enter admin WID: "))
    first_name = input("Enter admin first name: ")
    last_name = input("Enter admin last name: ")
    title = input("Enter title of admin: ")
    office = input("Enter office of admin: ")
    email = input("Enter admin email without @domain: ")
    cur.execute("INSERT INTO admin VALUES ('{}','{}','{}','{}','{}','{}')".format(wid, first_name, last_name, title, office, email))
    con.commit()


def course_insert():        # Admin
    CRN = int(input("Enter the 5 digit CRN related to the course: "))
    title = input("Enter the title of the class: ")
    department = input("Enter the department of the class: ")
    time = input("Enter the time frame of the class (i.e. 8-920): ")
    Days_of_week = input("Enter the days the classes take place on (M-monday, T-tuesday, W-Wednesday, TR-Thursday, F-Friday): ")
    semester = input("Enter the semester the class is during: ")
    year = int(input("Enter the year the class takes place in: "))
    credit = int(input("Enter the amount of credits the course is: "))
    cur.execute("INSERT INTO course VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(CRN, title, department, time, Days_of_week, semester, year, credit))
    con.commit()


def student_search():       # Admin/Teacher
    while True:
        print("What attribute will you filter for?\n"
              "1) First Name\n"
              "2) Last Name\n"
              "3) WID\n"
              "4) Major\n"
              "5) Graduation Year\n"
              "6) Email\n"
              "7) BACK")
        filter_op = int(input(''))
        if filter_op == 1:
            search_name = input("Enter the first name: ")
            cur.execute("SELECT * FROM student WHERE name = '{}'".format(search_name))
            for row in cur.fetchall():
                print(row)
        elif filter_op == 2:
            search_name = input("Enter the last name: ")
            cur.execute("SELECT * FROM student WHERE surname = '{}'".format(search_name))
            for row in cur.fetchall():
                print(row)
        elif filter_op == 3:
            search_wid = int(input("Enter WITid: "))
            cur.execute("SELECT * FROM student WHERE id = '{}'".format(search_wid))
            for row in cur.fetchall():
                print(row)
        elif filter_op == 4:
            search_major = input("Enter Major: ")
            cur.execute("SELECT * FROM student WHERE major = '{}'".format(search_major))
            for row in cur.fetchall():
                print(row)
        elif filter_op == 5:
            search_grad_year = int(input("Enter expected grad year: "))
            cur.execute("SELECT * FROM student WHERE gradyear = '{}'".format(search_grad_year))
            for row in cur.fetchall():
                print(row)

        elif filter_op == 6:
            search_email = input("Enter student email to search: ")
            cur.execute("SELECT * FROM student WHERE email = '{}'".format(search_email))
            for row in cur.fetchall():
                print(row)
        elif filter_op == 7:
            break
        else:
            print("Invalid Input!")


def teacher_search():       # Admin/Teacher
    while True:
        print("What attribute will you filter for?\n"
              "1) First Name\n"
              "2) Last Name\n"
              "3) WID\n"
              "4) Title\n"
              "5) Year Hired\n"
              "6) Email\n"
              "7) Department\n"
              "8) BACK")
        filter_op = int(input(''))
        if filter_op == 1:
            search_name = input("Enter the first name: ")
            cur.execute("SELECT * FROM instructor WHERE name = '{}'".format(search_name))
            for row in cur.fetchall():
                print(row)
        elif filter_op == 2:
            search_name = input("Enter the last name: ")
            cur.execute("SELECT * FROM instructor WHERE surname = '{}'".format(search_name))
            for row in cur.fetchall():
                print(row)
        elif filter_op == 3:
            search_wid = int(input("Enter WITid: "))
            cur.execute("SELECT * FROM instructor WHERE id = '{}'".format(search_wid))
            for row in cur.fetchall():
                print(row)
        elif filter_op == 4:
            search_title = input("Enter title: ")
            cur.execute("SELECT * FROM instructor WHERE title = '{}'".format(search_title))
            for row in cur.fetchall():
                print(row)
        elif filter_op == 5:
            search_hired_year = int(input("Enter year hired: "))
            cur.execute("SELECT * FROM instructor WHERE hireyear = '{}'".format(search_hired_year))
            for row in cur.fetchall():
                print(row)

        elif filter_op == 6:
            search_email = input("Enter instructor email to search: ")
            cur.execute("SELECT * FROM instructor WHERE email = '{}'".format(search_email))
            for row in cur.fetchall():
                print(row)
        elif filter_op == 7:
            search_depart = input("Enter department: ")
            cur.execute("SELECT * FROM instructor WHERE dept = '{}'".format(search_depart))
            for row in cur.fetchall():
                print(row)
            cur.execute("SELECT * FROM course WHERE department = '{}'".format(search_depart))
            for row in cur.fetchall():
                print(row)
        elif filter_op == 8:
            break
        else:
            print("Invalid Input!")


def admin_search():         # Admin
    while True:
        print("What attribute will you filter for?\n"
              "1) First Name\n"
              "2) Last Name\n"
              "3) WID\n"
              "4) Office\n"
              "5) Email\n"
              "6) Title\n"
              "7) BACK")
        filter_op = int(input(''))
        if filter_op == 1:
            search_name = input("Enter the first name: ")
            cur.execute("SELECT * FROM admin WHERE name = '{}'".format(search_name))
            for row in cur.fetchall():
                print(row)
        elif filter_op == 2:
            search_name = input("Enter the last name: ")
            cur.execute("SELECT * FROM admin WHERE surname = '{}'".format(search_name))
            for row in cur.fetchall():
                print(row)
        elif filter_op == 3:
            search_wid = int(input("Enter WITid: "))
            cur.execute("SELECT * FROM admin WHERE id = '{}'".format(search_wid))
            for row in cur.fetchall():
                print(row)
        elif filter_op == 4:
            search_office = input("Enter Office: ")
            cur.execute("SELECT * FROM admin WHERE office = '{}'".format(search_office))
            for row in cur.fetchall():
                print(row)
        elif filter_op == 5:
            search_email = input("Enter student email to search: ")
            cur.execute("SELECT * FROM admin WHERE email = '{}'".format(search_email))
            for row in cur.fetchall():
                print(row)
        elif filter_op == 6:
            search_title = input("Enter title: ")
            cur.execute("SELECT * FROM admin WHERE title = '{}'".format(search_title))
            for row in cur.fetchall():
                print(row)
        elif filter_op == 7:
            break
        else:
            break


def course_search():        # Everyone
    while True:
        print("What attribute will you filter for?\n"
              "1) CRNs\n"
              "2) Title\n"
              "3) Department\n"
              "4) Semester\n"
              "5) BACK")
        course_op = int(input(''))
        if course_op == 1:
            search_crn = int(input("Enter CRN: "))
            cur.execute("SELECT * FROM course WHERE crn = '{}'".format(search_crn))
            for row in cur.fetchall():
                print(row)
        elif course_op == 2:
            search_title = input("Enter Title: ")
            cur.execute("SELECT * FROM course WHERE title = '{}'".format(search_title))
            for row in cur.fetchall():
                print(row)
        elif course_op == 3:
            search_depart = input("Enter department : ")
            cur.execute("SELECT * FROM course WHERE department  = '{}'".format(search_depart))
            for row in cur.fetchall():
                print(row)
            cur.execute("SELECT * FROM instructor WHERE dept = '{}'".format(search_depart))
            for row in cur.fetchall():
                print(row)
        elif course_op == 4:
            search_semester = input("Enter semester : ")
            cur.execute("SELECT * FROM course WHERE semester = '{}'".format(search_semester))
            for row in cur.fetchall():
                print(row)
        elif course_op == 5:
            break
        else:
            print("Invalid Input!")


def edit_student_attributes():      # Admin
    while True:
        print("What attribute would you like to change?\n"
              "1) WID\n"
              "2) First Name\n"
              "3) Last Name\n"
              "4) Graduation Year\n"
              "5) Major\n"
              "6) BACK")
        student_edit_op = int(input(''))
        if student_edit_op == 1:
            old_wid = int(input("What WID will you change? "))
            new_wid = int(input("What WID will replace it? "))
            cur.execute("UPDATE student SET id = '{}' WHERE id = '{}'".format(new_wid, old_wid))
            con.commit()
        elif student_edit_op == 2:
            old_name = input("What first name will you change? ")
            new_name = input("What first name will replace it? ")
            cur.execute("UPDATE student SET name = '{}' WHERE name = '{}'".format(new_name, old_name))
            con.commit()
        elif student_edit_op == 3:
            old_surname = input("What last name will you change? ")
            new_surname = input("What last name will replace it? ")
            cur.execute("UPDATE student SET surname = '{}' WHERE surname ='{}'".format(new_surname, old_surname))
            con.commit()
        elif student_edit_op == 4:
            name = input("Who are you editing? ")
            # old_grad_year = int(input("What Year will you change? "))
            new_grad_year = int(input("What year will replace it? "))
            cur.execute("UPDATE student SET gradyear = '{}' WHERE name ='{}'".format(new_grad_year, name))
            con.commit()
        elif student_edit_op == 5:
            name = input("Who are you editing? ")
            # old_major = input("What major will you change? ")
            new_major = input("What major will replace it? ")
            cur.execute("UPDATE student SET major = '{}' WHERE name = '{}'".format(new_major, name))
            con.commit()

        elif student_edit_op == 6:
            break
        else:
            print("Invalid Input!")


def edit_teacher_attributes():          # Admin
    while True:
        print("What attribute would you like to change?\n"
              "1) WID\n"
              "2) First Name\n"
              "3) Last Name\n"
              "4) Year Hired\n"
              "5) Title\n"
              "6) Department\n"
              "7) BACK")
        student_edit_op = int(input(''))
        if student_edit_op == 1:
            old_wid = int(input("What WID will you change? "))
            new_wid = int(input("What WID will replace it? "))
            cur.execute("UPDATE instructor SET id = '{}' WHERE id = '{}'".format(new_wid, old_wid))
            con.commit()
        elif student_edit_op == 2:
            old_name = input("What first name will you change? ")
            new_name = input("What first name will replace it? ")
            cur.execute("UPDATE instructor SET name = '{}' WHERE name = '{}'".format(new_name, old_name))
            con.commit()
        elif student_edit_op == 3:
            old_surname = input("What last name will you change? ")
            new_surname = input("What last name will replace it? ")
            cur.execute("UPDATE instructor SET surname = '{}' WHERE surname ='{}'".format(new_surname, old_surname))
            con.commit()
        elif student_edit_op == 4:
            name = input("Who are you editing? ")
            new_hire_year = int(input("What year will replace it? "))
            cur.execute("UPDATE instructor SET hireyear = '{}' WHERE name ='{}'".format(new_hire_year, name))
            con.commit()
        elif student_edit_op == 5:
            name = input("Who are you editing? ")
            new_title = input("What title will replace it? ")
            cur.execute("UPDATE instructor SET title = '{}' WHERE name = '{}'".format(new_title, name))
            con.commit()
        elif student_edit_op == 6:
            name = input("Who are you editing? ")
            new_depart = input("What department will replace it? ")
            cur.execute("UPDATE instructor SET dept = '{}' WHERE name = '{}'".format(new_depart, name))
            con.commit()
        elif student_edit_op == 7:
            break
        else:
            print("Invalid Input!")


def edit_admin_attributes():        # Admin
    while True:
        print("What attribute would you like to change?\n"
              "1) WID\n"
              "2) First Name\n"
              "3) Last Name\n"
              "4) Title\n"
              "5) Office\n"
              "6) BACK")
        student_edit_op = int(input(''))
        if student_edit_op == 1:
            old_wid = int(input("What WID will you change? "))
            new_wid = int(input("What WID will replace it? "))
            cur.execute("UPDATE admin SET id = '{}' WHERE id = '{}'".format(new_wid, old_wid))
            con.commit()
        elif student_edit_op == 2:
            old_name = input("What first name will you change? ")
            new_name = input("What first name will replace it? ")
            cur.execute("UPDATE admin SET name = '{}' WHERE name = '{}'".format(new_name, old_name))
            con.commit()
        elif student_edit_op == 3:
            old_surname = input("What last name will you change? ")
            new_surname = input("What last name will replace it? ")
            cur.execute("UPDATE admin SET surname = '{}' WHERE surname ='{}'".format(new_surname, old_surname))
            con.commit()
        elif student_edit_op == 4:
            name = input("Who are you editing? ")
            new_title = input("What title will replace it? ")
            cur.execute("UPDATE admin SET title = '{}' WHERE name ='{}'".format(new_title, name))
            con.commit()
        elif student_edit_op == 5:
            name = input("Who are you editing? ")
            new_office = input("What office will replace it? ")
            cur.execute("UPDATE admin SET office = '{}' WHERE name = '{}'".format(new_office, name))
            con.commit()

        elif student_edit_op == 6:
            break
        else:
            print("Invalid Input!")


def edit_course_attributes():           # Admin
    while True:
        print("What attribute would you like to change?\n"
              "1) CRN\n"
              "2) Title\n"
              "3) Department\n"
              "4) Time\n"
              "5) Days of the Week\n"
              "6) Semester\n"
              "7) Year\n"
              "8) Credits\n"
              "9) BACK")
        student_edit_op = int(input(''))
        if student_edit_op == 1:
            old_crn = int(input("What CRN will you change? "))
            new_crn = int(input("What CRN will replace it? "))
            cur.execute("UPDATE course SET crn = '{}' WHERE crn = '{}'".format(new_crn, old_crn))
            con.commit()
        elif student_edit_op == 2:
            old_title = input("What title name will you change? ")
            new_title = input("What title name will replace it? ")
            cur.execute("UPDATE course SET title = '{}' WHERE title = '{}'".format(new_title, old_title))
            con.commit()
        elif student_edit_op == 3:
            course = input("What courses department will you change? ")
            new_depart = input("What department will replace it? ")
            cur.execute("UPDATE course SET department = '{}' WHERE title ='{}'".format(new_depart, course))
            con.commit()
        elif student_edit_op == 4:
            course = input("What course time will you change? ")
            new_time = input("What time frame will replace it?(i.e. 8-920) ")
            cur.execute("UPDATE course SET time = '{}' WHERE title ='{}'".format(new_time, course))
            con.commit()
        elif student_edit_op == 5:
            course = input("What courses days will you change? ")
            new_days = input("What days will replace it? ")
            cur.execute("UPDATE course SET dotw = '{}' WHERE title ='{}'".format(new_days, course))
            con.commit()
        elif student_edit_op == 6:
            course = input("What courses semester will you change? ")
            new_semester = input("What semester will replace it? ")
            cur.execute("UPDATE course SET semester = '{}' WHERE title ='{}'".format(new_semester, course))
            con.commit()
        elif student_edit_op == 7:
            course = input("What courses year will you change? ")
            new_year = input("What year will replace it? ")
            cur.execute("UPDATE course SET year = '{}' WHERE title ='{}'".format(new_year, course))
            con.commit()
        elif student_edit_op == 8:
            course = input("What courses credits will you change? ")
            new_credits = input("What credits will replace it? ")
            cur.execute("UPDATE course SET credits = '{}' WHERE title ='{}'".format(new_credits, course))
            con.commit()
        elif student_edit_op == 9:
            break
        else:
            print("Invalid Input!")



get_student_data()
get_teacher_data()
get_admin_data()
j = 0

# Login system
while True:
    id_in = int(input('Please enter your ID number: '))
    name_in = input('Please enter your first name: ')
    for student in student_database:
        if id_in == student.id and name_in == student.first_name :
            print('Successful login')
            j = 1
    for teacher in teacher_database:
        if id_in == teacher.id and name_in == teacher.first_name:
            print('Successful login')
            j = 2
    for admin in admin_database:
        if id_in == admin.id and name_in == admin.first_name:
            print('Successful login')
            j = 3
    if j == 0:
        print('error')
    else:
        break


# Main


while True:
    print("============================\n"
          "   Assignment 3 Database\n"
          "============================")
    print("What would you like to do?\n"
          "1) Search Database\n"
          "2) Insert/Remove into database\n"
          "3) Display Database\n"
          "4) Create Table(courses)\n"
          "5) Edit specifics database\n"
          "6) EXIT\n")
    option = int(input(''))

    if option == 1:
        while True:
            print("What database would you like to search?\n"
                  "1) Student\n"
                  "2) Teacher\n"
                  "3) Admin\n"
                  "4) Courses\n"
                  "5) BACK")
            search_op = int(input(''))
            if search_op == 1:
                student_search()
            elif search_op == 2:
                teacher_search()
            elif search_op == 3:
                admin_search()
            elif search_op == 4:
                course_search()
            elif search_op == 5:
                break
            else:
                print("Invalid Input!")

    elif option == 2 and j == 3:
        while True:
            print("Would you like to Insert or Remove?\n"
                  "1) Insert\n"
                  "2) Remove\n"
                  "3) Back\n")
            choice = int(input(''))
            if choice == 1:
                print("Which database would you like to add to?\n"
                      "1) Student\n"
                      "2) Instructor\n"
                      "3) Admin\n"
                      "4) Courses\n"
                      "5) BACK\n")
                insert_op = int(input(''))
                if insert_op == 1:
                    student_insert()
                elif insert_op == 2:
                    teacher_insert()
                elif insert_op == 3:
                    admin_insert()
                elif insert_op == 4:
                    course_insert()
                elif insert_op == 5:
                    break
                else:
                    print("Invalid Input!")
            elif choice == 2:
                print("Which database would you like to remove from?\n"
                      "1) Student\n"
                      "2) Instructor\n"
                      "3) Admin\n"
                      "4) Courses\n"
                      "5) BACK\n")
                remove_op = int(input(''))
                if remove_op == 1:
                    student_name = input("Enter the name of the student you would like to remove: ")
                    cur.execute("DELETE FROM student WHERE name = '{}'".format(student_name))
                    print(f"Student {student_name} was removed from the Database!")
                    con.commit()
                elif remove_op == 2:
                    instructor_name = input("Enter the name of the teacher you would like to remove: ")
                    cur.execute("DELETE FROM instructor WHERE name = '{}'".format(instructor_name))
                    print(f"Teacher {instructor_name} was removed from the Database!")
                    con.commit()
                elif remove_op == 3:
                    admin_name = input("Enter the name of the admin you would like to remove: ")
                    cur.execute("DELETE FROM admin WHERE name = '{}'".format(admin_name))
                    print(f"Admin {admin_name} was removed from the Database!")
                    con.commit()
                elif remove_op == 4:
                    course_name = input("Enter the name of the course you would like to remove: ")
                    cur.execute("DELETE FROM course WHERE name = '{}'".format(course_name))
                    print(f"Course {course_name} was removed from the Database!")
                    con.commit()
                elif remove_op == 5:
                    break
                else:
                    print("Invalid Input!")
            elif choice == 3:
                break
            else:
                print("Invalid input!")

    elif option == 3:
        while True:
            print("What database would you like to see?\n"
                  "1) Student Database\n"
                  "2) Instructor Database\n"
                  "3) Admin Database\n"
                  "4) Course Database\n"
                  "5) Display All Databases\n"
                  "6) BACK\n")
            print_op = int(input(''))

            if print_op == 1:
                display_student()
            elif print_op == 2:
                display_teachers()
            elif print_op == 3:
                display_admin()
            elif print_op == 4:
                display_courses()
            elif print_op == 5:
                display_all_table()
            elif print_op == 6:
                break
            else:
                print("Invalid option!")

    elif option == 4:
        print("Would you like to create the course database?\n"
              "1) Yes\n"
              "2) No\n")
        create_table_op = int(input(''))
        if create_table_op == 1:
            create_course_table()
        elif create_table_op == 2:
            break
        else:
            print("Invalid Input!")

    elif option == 5:
        while True:
            print("Which database would you like to edit?\n"
                  "1) Student\n"
                  "2) Teacher\n"
                  "3) Admin\n"
                  "4) Course\n"
                  "5) BACK\n")
            edit_op = int(input(''))
            if edit_op == 1:
                edit_student_attributes()
            elif edit_op == 2:
                edit_teacher_attributes()
            elif edit_op == 3:
                edit_admin_attributes()
            elif edit_op == 4:
                edit_course_attributes()
            elif edit_op == 5:
                break
            else:
                print("Invalid Input!")

    elif option == 6:
        print("GOODBYE!")
        exit()
    else:
        print("Invalid Input!")
