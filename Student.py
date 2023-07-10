from User import *


class Student(User):
    def __init__(self, id, first_name, last_name, email, grad_year, major):
        super().__init__(id, first_name, last_name, email)
        self.grad_year = grad_year
        self.major = major

    # Functions for add / remove crn
    def add(self, in_crn):
        self.crn.append(in_crn)
        print('CRN: ', in_crn, ' Added!')

    def remove(self, in_crn):
        i = 0
        j = 0
        while i < len(self.crn):
            if self.crn[i] == in_crn:
                self.crn.remove(in_crn)
                print('CRN: ', in_crn, 'Removed!')
                j = 1
            i = i + 1
        if j == 0:
            print('Could not find: ', in_crn)

    def show_schedule(self):
        i = 0
        while i < len(self.crn):
            print(self.crn[i])
            i = i + 1

