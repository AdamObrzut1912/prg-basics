from contact import Contact

class Contact_List():
    def __init__(self):
        self.contacts_list = []

    def add_contact(self, name, email, telefone):
        self.new_contact = Contact(name, email, telefone)
        self.contacts_list.append(self.new_contact)

    def display_contacts(self):
        for i in self.contacts_list:
            print(i)