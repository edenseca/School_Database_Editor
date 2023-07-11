from User import *


class Teacher(User):
    def __init__(self, id, first_name, last_name, email, title, hire_year, department):
        super().__init__(id, first_name, last_name, email)
        self.title = title
        self.hire_year = hire_year
        self.department = department

    def show_schedule(self):
        def course_search():  # Everyone
            while True:
                print("What attribute will you filter for?\n"
                      "1) CRNs\n"
                      "2) Title\n"
                      "3) Department\n"
                      "4) Semester\n"
                      "5) Exit")
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


    def print_class_list(self):
        def display_student():  # Teachers
            cur.execute("SELECT * FROM student")
            t = cur.fetchall()

            print("STUDENTS:")
            for row in t:
                print(row)

    def search_crn(self):
        def display_courses(self):  # Everyone
            cur.execute("SELECT * FROM course")
            z = cur.fetchall()

            print("COURSES:")
            for row in z:
                print(row)




    def student_search():  # Admin/Teacher
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
