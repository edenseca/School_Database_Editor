from User import *


class Teacher(User):
    def __init__(self, id, first_name, last_name, email, title, hire_year, department):
        super().__init__(id, first_name, last_name, email)
        self.title = title
        self.hire_year = hire_year
        self.department = department

    def show_schedule(self):
        print('Showing Teachers Schedule')
        self.id_num = self.id_num

    def print_class_list(self):
        print('Printing Class list')
        self.id_num = self.id_num

    def search_crn(self):
        print('Search for CRN')
        self.id_num = self.id_num
