from User import *
import sqlite3
con = sqlite3.connect('assignment3.db')
cur = con.cursor()


class Student(User):

    def __init__(self, id, first_name, last_name, email, grad_year, major, crn):
        super().__init__(id, first_name, last_name, email)
        self.grad_year = grad_year
        self.major = major
        self.crn = []

    # Functions for add / remove crn
    def add(self):
        in_crn = input("Please type in your CRN: \n")
        self.crn.append(in_crn)
        print('CRN: ', in_crn, ' Added!')

    def remove(self):
        in_crn = int(input('Enter CRN: '))
        self.crn.append(in_crn)
        print("CRN: ", in_crn, " Removed!")

    def course_search(self):  # Everyone
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

    def display_courses(self):  # Everyone
        cur.execute("SELECT * FROM course")
        z = cur.fetchall()

        print("COURSES:")
        for row in z:
            print(row)

