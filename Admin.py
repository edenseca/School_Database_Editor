from User import *


class Admin(User):
    def __init__(self, id, first_name, last_name, email, title, office):
        super().__init__(id, first_name, last_name, email)
        self.title = title
        self.office = office

    def add_course(self):
        print('Enter CRN to add to system: ')
        self.id_num = self.id_num

    def remove_course(self):
        print('Enter CRN to remove from system: ')
        self.id_num = self.id_num

    def add_remove_student(self):
        print('Enter Students Name: ')
        self.id_num = self.id_num

    def search_roaster(self):
        print('Enter CRN to see Roaster: ')
        self.id_num = self.id_num
