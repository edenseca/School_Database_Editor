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
    cur.execute("CREATE TABLE course(CRN, title, dept, time, dotw, semester, year, credits)")
    cur.execute("""
        INSERT INTO course VALUES
            ('40001', 'Physics', 'BSAS', '8-920', 'MWF', 'Fall', '2024', '4' ),
            ('40002', 'Physics 2', 'BSCO', '2-320', 'TTR', 'Spring', '2024', '4' ),
            ('40003', 'Calculus', 'BCOS', '8-920', 'MWF', 'Fall', '2024', '4' ),
            ('40004', 'Calculus 2', 'BSEE', '10-1120', 'MWF', 'Spring', '2024', '4' ),
            ('40005', 'Psychology', 'HUSS', '10-12', 'TTR', 'Fall', '2024', '2' )
    """)
    con.commit()


# def display_all_table():    # Not needed
#     display_student()
#     display_teachers()
#     display_admin()
#     display_courses()


get_student_data()
get_teacher_data()
get_admin_data()

j = 0

# Login system
for u in range (3):
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
        if j == 1:  # Student
            print("Student Actions:")
            print("Choose one (1-4)")
            print("1) Print Schedule")
            print("2) Add Course")
            print("3) Drop Course")
            print("4) Search Course")
            print("5) Exit")
            choice2 = int(input())
            if choice2 == 1:
                student.display_courses()
            elif choice2 == 2:
                student.add()
            elif choice2 == 3:
                student.remove()
            elif choice2 == 4:
                student.course_search()
            elif choice2 == 5:
                break
            else:
                print("Invalid choice.")

        elif j == 2:  # Instructor
            print("Instructor Actions:")
            print("Choose one (1-3)")
            print("1) Print Schedule")
            print("2) Print Class List")
            print("3) Search Courses")
            print("4) Exit")
            choice2 = int(input())

            if choice2 == 1:
                teacher.print_schedule()
            elif choice2 == 2:
                teacher.print_class_list()
            elif choice2 == 3:
                teacher.search_courses()
            elif choice2 == 4:
                break
            else:
                print("Invalid choice.")

        elif j == 3:  # Admin
            print("Admin Actions:")
            print("Choose one (1-4)")
            print("1) Add to Database")
            print("2) Remove from Database")
            print("3) Search and Print Rosters and Courses")
            print("4) Exit")
            choice2 = int(input())

            if choice2 == 1:
                while True:
                    print("Which database would you like to add to?\n"
                          "1) Student\n"
                          "2) Instructor\n"
                          "3) Admin\n"
                          "4) Courses\n"
                          "5) Exit\n")
                    insert_op = int(input(''))
                    if insert_op == 1:
                        admin.student_insert()
                    elif insert_op == 2:
                        admin.teacher_insert()
                    elif insert_op == 3:
                        admin.admin_insert()
                    elif insert_op == 4:
                        admin.course_insert()
                    elif insert_op == 5:
                        break
                    else:
                        print("Invalid Input!")
            elif choice2 == 2:      # CHANGE TO REMOVE FROM DATABASES
                while True:
                    print("Which database would you like to remove from?\n"
                          "1) Student\n"
                          "2) Instructor\n"
                          "3) Admin\n"
                          "4) Courses\n"
                          "5) Exit\n")
                    insert_op = int(input(''))
                    if insert_op == 1:
                        admin.student_remove()
                    elif insert_op == 2:
                        admin.teacher_remove()
                    elif insert_op == 3:
                        admin.admin_remove()
                    elif insert_op == 4:
                        admin.remove_courses()
                    elif insert_op == 5:
                        break
                    else:
                        print("Invalid Input!")
            elif choice2 == 3:
                while True:
                    print("Would you like to search or print students/courses?\n"
                          "1) Print\n"
                          "2) Search\n"
                          "3) Exit\n")
                    search_print_op = int(input(""))
                    if search_print_op == 1:
                        print("Would you like to print students or courses?\n"
                              "1) Students\n"
                              "2) Courses\n"
                              "3) Exit\n")
                        print_op = int(input(""))
                        if print_op == 1:
                            admin.print_class_list()
                        elif print_op == 2:
                            admin.display_courses()
                        elif print_op == 3:
                            break
                        else:
                            print("Invalid Input!")
                    elif search_print_op == 2:
                        print("Would you like to search students or courses?\n"
                              "1) Students\n"
                              "2) Courses\n"
                              "3) Exit\n")
                        search_op = int(input(""))
                        if search_op == 1:
                            admin.student_search()
                        elif search_op == 2:
                            admin.course_search()
                        elif search_op == 3:
                            break
                        else:
                            print("Invalid Input!")
                    elif search_print_op == 3:
                        break
                    else:
                        print("Invalid Input!")
            elif choice2 == 4:
                break
            else:
                print("Invalid choice.")