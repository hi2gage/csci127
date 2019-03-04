# -----------------------------------------------------
# CSCI 127, Lab 8
# March 7, 2019
# Gage Halverson
# -----------------------------------------------------
class Contact:
    #creates new instance
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.title = ""

    #prints name and phone_number
    def print_entry(self):
        #checks to see if title is defined yet
        if len(self.title) != 0:
            name = self.title + " " + self.first_name + " " + self.last_name
        else:
            name = self.first_name + " " + self.last_name
            
        #prints in correct format
        print("{0:24} {1}".format(name, self.phone_number))

    #sets new first_name
    def set_first_name(self, new_first):
        self.first_name = new_first

    #sets title of instance
    def set_title(self, title):
        self.title = title

    #returns phone_number
    def get_cell_number(self):
        return self.phone_number

    #returns first 3 digits of phone_number
    def get_area_code(self):
        return self.phone_number[:3]
# -----------------------------------------------------
# Do not change anything below this line
# -----------------------------------------------------

def print_directory(contacts):
    print("My Contacts")
    print("-----------")
    for person in contacts:
        person.print_entry()
    print("-----------\n")

# -----------------------------------------------------

def main():
    champ = Contact("???", "Bobcat", "406-994-0000")
    president = Contact("Waded", "Cruzado", "406-994-CATS")
    professor = Contact("John", "Paxton", "406-994-4780")

    contacts = [champ, president, professor]

    print_directory(contacts)

    champ.set_first_name("Champ")
    president.set_title("President")
    professor.set_title("Professor")

    print_directory(contacts)

    print("The area code for cell number", champ.get_cell_number(), "is", \
           champ.get_area_code())

# -----------------------------------------------------

main()
