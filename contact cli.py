import pickle
import os

class Contact:
    def __init__(self, fname, lname,email, phone):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone

    def __str__(self):
        return "First Name:{0}\nLast Name:{1}\nEmail address:{2}\nPhone:{3}".format(self.fname,self.lname, self.email, self.phone)

    def change_fname(self, fname):
        self.fname = fname
    def change_lname(self, lname):
        self.lname = lname
    def change_email(self, email):
        self.email = email
    def change_phone(self, phone):
        self.phone = phone


def add_contact():
    test = open("test", "rb")
    is_file_empty = os.path.getsize("test") == 0
    if not is_file_empty:
        list_contacts = pickle.load(test)
    else:
        list_contacts = []
    try:
        contact = get_contact_info_from_user()
        test = open("test", "wb")
        list_contacts.append(contact)
        pickle.dump(list_contacts, test)
        print ("Contact added")
    except KeyboardInterrupt:
        print ("Contact not added")
    except EOFError:
        print ("Contact not added")
    finally:
        test.close()


def get_contact_info_from_user():
    try:
        contact_fname = input("Enter contact first name\n")
        contact_lname = input("Enter contact last name\n")
        contact_email = input("Enter contact email\n")
        contact_phone = input("Enter contact phone number\n")
        contact = Contact(contact_fname, contact_lname, contact_email, contact_phone)
        return contact
    except EOFError as e:
        # print "You entered end of file. Contact not added"
        raise e
    except KeyboardInterrupt as e:
        # print "Keyboard interrupt. Contact not added"
        raise e


def display_contacts():
    test = open("test", "rb")
    is_file_empty = os.path.getsize("test") ==0
    if not is_file_empty:
        list_contacts = pickle.load(test)
        for each_contact in list_contacts:
            print ("first name: "+" " +each_contact.fname)
            print("Last name: "+" " +each_contact.lname)
            print ("Email: "+" " +each_contact.email)
            print("Phone number: "+" " +each_contact.phone+ "\n")
    else:
        print ("No contacts in address book")
        return
    test.close()


def search_contact():
    test = open("test", "rb")
    is_file_empty = os.path.getsize("test") ==0
    if not is_file_empty:
        search_fname = input("Enter the first name\n")
        is_contact_found = False
        list_contacts = pickle.load(test)
        for each_contact in list_contacts:
            contact_fname = each_contact.fname
            search_fname = search_fname.lower()
            contact_fname = contact_fname.lower()
            if (contact_fname == search_fname):
                print (each_contact)
                is_contact_found = True
                break
        if not is_contact_found:
            print ("No contact found with the provided search name")
    else:
        print ("Address book empty. No contact to search")
    test.close()


def delete_contact():
    test = open("test", "rb")
    is_file_empty = os.path.getsize("test") ==0
    if not is_file_empty:
        fname = input("Enter the first name of the contact to be deleted\n")
        list_contacts = pickle.load(test)
        is_contact_deleted = False
        for i in range(0, len(list_contacts)):
            each_contact = list_contacts[i]
            if each_contact.fname == fname:
                del list_contacts[i]
                is_contact_deleted = True
                print (fname + "has been deleted")
                test = open("test", "wb")
                if (len(list_contacts) == 0):
                    test.write(b"")
                else:
                    pickle.dump(list_contacts, test)
                break
        if not is_contact_deleted:
            print ("No contact with this name found")

    else:
        print ("Address book empty. No contact to delete")
    test.close()


def modify_contact():
    test = open("test", "rb")
    is_file_empty = os.path.getsize("test") ==0
    if not is_file_empty:
        fname = input("Enter the first name of the contact to be modified\n")
        list_contacts = pickle.load(test)
        is_contact_modified = False
        for each_contact in list_contacts:
            if each_contact.fname == fname:
                do_modification(each_contact)
                test = open("test", "wb")
                pickle.dump(list_contacts, test)
                is_contact_modified = True
                print ("Contact modified")
                break
        if not is_contact_modified:
            print ("No contact with this name found")
    else:
        print ("Address book empty. No contact to delete")
    test.close()


def do_modification(contact):
    try:
        while True:
            print ("Enter 1 to modify lastname and 2 to modify email address and 3 to change contact number")
            choice = input()
            if (choice == "1"):
            	new_lname = input("Enter new last name")
            	contact.change_lname(new_lname)
            	break
            if (choice == "2"):
                new_email = input("Enter new email address\n")
                contact.change_email(new_email)
                break
            elif (choice == "3"):
                new_phone = input("Enter new phone number\n")
                contact.change_phone(new_phone)
                break
            else:
                print ("Incorrect choice")
                break
    except EOFError:
        print ("EOF Error occurred")
    except KeyboardInterrupt:
        print ("KeyboardInterrupt occurred")
print ("Enter 'a' to add a contact, 'b' to browse through contacts, 'd' to delete a contact, 'm' to modify a contact, 's' to search for contact and 'q' to quit")
while True:
    choice=input("Enter your choice\n")
    if choice == 'q':
        break
    elif(choice=='a'):
        add_contact()
    elif(choice=='b'):
        display_contacts()
    elif(choice=='d'):
        delete_contact()
    elif(choice=='m'):
        modify_contact()
    elif(choice=='s'):
        search_contact()
    else:
        print ("Incorrect choice. Need to enter the choice again")