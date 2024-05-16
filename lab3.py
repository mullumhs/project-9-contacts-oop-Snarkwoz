"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Enhance the Contact class by adding instance and class methods.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 1. Copy/paste your Contact class from Lab 2.        
# 2. Add a check_email method to check if the email contains an '@'
# 3. Create a class method get_contact_count to retrieve the number of contacts
# 4. Reproduce the instances of the Contact class that you created in Lab 2
# 5. Call your new instance method on one Contact and print the result
# 6. Use the class method to print out the total number of contacts
class Contact:
    num_of_contacts = 0
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        Contact.num_of_contacts += 1

    def check_email(self):
        if "@" in self.email:
            print(f"{self.email} is valid")
            return True
        else:
            print(f"{self.email} is not valid")
            return False
    
    @classmethod
    def get_contact_count(self):
        return self.num_of_contacts
        

jeremy = Contact("Jeremy", "0469492956", "jeremy@idontknowlmao.com")
tyrannasourus_rex = Contact("Rex", "56723592543", "tyrannasourus.rex@iminthejurassicperiodwhydoihaveanemail.com")

print(f"{jeremy.name}: {jeremy.phone_number}, {jeremy.email}")
print(f"{tyrannasourus_rex.name}: {tyrannasourus_rex.phone_number}, {tyrannasourus_rex.email}")
tyrannasourus_rex.check_email()
print(jeremy.num_of_contacts)
