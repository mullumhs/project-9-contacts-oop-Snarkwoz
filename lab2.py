"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a class for a contact in a contact management system.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a class named Contact that represents a contact in a contact management system. 
# This class should have an initialiser with attributes for name, phone_number, and email.
# Add a class attribute to keep track of the total number of contacts.

class Contact:
    num_of_contacts = 0
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        Contact.num_of_contacts += 1

# Create at least two instances of the Contact class with different data.

jeremy = Contact("Jeremy", "0469492956", "jeremy@idontknowlmao.com")
tyrannasourus_rex = Contact("Rex", "56723592543", "tyrannasourus.rex@iminthejurassicperiodwhydoihaveanemail.com")

# Write code that prints out the details of each contact you have created.

print(f"{jeremy.name}: {jeremy.phone_number}, {jeremy.email}")
print(f"{tyrannasourus_rex.name}: {tyrannasourus_rex.phone_number}, {tyrannasourus_rex.email}")
print(jeremy.num_of_contacts)