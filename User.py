# Parent class
class User:
    def __init__(self, id, first_name, last_name, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def show_first_name(self):
        return self.first_name

    def show_sur_name(self):
        return self.last_name

    def show_id_num(self):
        return self.id_num

    def show_details(self):
        print(f'{self.first_name}')
        print(f'{self.last_name}')
        print(f'{self.id_num}')
