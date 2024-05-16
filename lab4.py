"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 4
---------------------------------------------------------------------------------
- File Name: lab4.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Implement the ContactManager class and perform CRUD operations.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 1. Import the ContactManager class here.

from contact_manager import ContactManager
CM = ContactManager()

# 2. Go to the 'contact_manager.py' file and implement the TODO in the display_contacts method.



# 3. Create two contacts using the ContactManager.

contact1 = CM.add_contact("Jack", "57923759", "jack@theripper.com")
contact2 = CM.add_contact("idk", "385923659267598", "somerandomemail@emailplace.com")

# 4. Display all contacts.

print(CM)

# 5. Update the email address of one contact.

CM.update_contact("idk", new_phone="567385238", new_email="vbefbhaise@feiufha.com")

# 6. Remove one of the contacts.

CM.remove_contact("Jack")

# 7. Display all contacts again.

print(CM)
print("-"*40)