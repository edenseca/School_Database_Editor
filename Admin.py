from User import *


class Admin(User):
    def __init__(self, id, first_name, last_name, email, title, office):
        super().__init__(id, first_name, last_name, email)
        self.title = title
        self.office = office

    def add_course(self):
        print('Enter CRN to add to system: ')
        self.id = self.id

    def remove_course(self):
        print('Enter CRN to remove from system: ')
        self.id = self.id

    def add_remove_student(self):
        print('Enter Students Name: ')
        self.id = self.id

    def search_roaster(self):
        print('Enter CRN to see Roaster: ')
        self.id = self.id
