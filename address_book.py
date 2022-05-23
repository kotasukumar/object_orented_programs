class Contact(object):
    contact_list = []

    def __init__(self, name=None, address=None, email=None, mobile_number=None):
        self.name = name
        self.address = address
        self.email = email
        self.mobile_number = mobile_number

    def add_contact(self):
        temp = [str(input("Enter name of the person: ")), str(input("Enter address of the person: ")),
                str(input("Enter email id of the person: ")), int(input("Enter number of the person: "))]
        self.contact_list.append(temp)

    def remove_contact(self, contact_name):
        for i in range(len(self.contact_list)):
            if self.contact_list[i][0] == contact_name:
                self.contact_list.remove(self.contact_list[i])

    def update(self, name, parameter):
        for i in range(len(self.contact_list)):
            if self.contact_list[i][0] == name:
                if parameter == 1:
                    self.contact_list[i][0] = str(input("Enter the new name: "))
                elif parameter == 2:
                    self.contact_list[i][1] = str(input("Enter the new address: "))
                elif parameter == 3:
                    self.contact_list[i][2] = str(input("Enter the new email id: "))
                elif parameter == 4:
                    self.contact_list[i][3] = int(input("Enter the new number: "))


if __name__ == "__main__":
    contact_details = Contact()
    while True:
        try:
            choice = int(
                input("1 - add contact\n2 - remove contact\n3 - display\n4 - update\n5 - exit\nEnter your choice: "))
            assert choice <= 5
        except AssertionError:
            print("please enter number between 1 to 5")
        except ValueError:
            print("Please enter a integer")

        if choice == 1:
            contact_details.add_contact()
            print("added successfully")
        elif choice == 2:
            contact_details.remove_contact(str(input("Enter name of the person to remove: ")))
            print("removed successfully")
        elif choice == 3:
            print(contact_details.contact_list)
        elif choice == 4:
            try:
                contact_details.update((str(input("Enter name of the contact you need to update: "))),
                                       int(input("\n1 - name\n2 - address\n3 - email id\n4 - number\nEnter your "
                                                 "choice to update: ")))
            except ValueError:
                print("please enter correct input")
            print("updated successfully")
        elif choice == 5:
            break
