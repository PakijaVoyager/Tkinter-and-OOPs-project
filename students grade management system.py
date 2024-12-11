import sys #sys module is imported to exit from the program using exit() function
class Information: #Intializing class
    def __init__(self): #Initializing constructor
        self.student_dicts={} #Initializing instance varialble as empty dictionary
        self.main() #When the object of this class will be created then the main method will automatically called
    
    def main(self): #This method ask user for performing different functionality.
        ask_usr = int(input("Enter \n1 : Add\n2 : Update\n3 : Delete\n4 : View\n5 : Exit\n:"))
        if ask_usr == 1:
            self.add_items()
        
        elif ask_usr == 2:
            self.update_item()
        
        elif ask_usr == 3:
            self.del_item()
        
        elif ask_usr == 4:
            self.view_item()
        
        elif ask_usr == 5:
            sys.exit()
    
        else:
            print(f"{ask_usr} not in the option")

#Below it different methods are defined for adding , deleting , updating , viewing students name and grade.
###############################################################################
    def add_items(self):
        ask_name = input("Enter your name : ")
        ask_grade = int(input("Enter your grade : "))
        self.student_dicts[ask_name] = ask_grade
        print(f"{ask_name} with grade {ask_grade} has been successfully added")
        self.main()

    def update_item(self):
        ask_name = input("Enter your name : ")
        ask_grade = int(input("Enter grade to update : "))
        if ask_name in self.student_dicts:
            self.student_dicts[ask_name] = ask_grade

        else:
            print(f"{ask_name} is not in the list")
        self.main()


    def del_item(self):
        ask_name = input("Enter your name : ")
        if ask_name in self.student_dicts:
            del self.student_dicts[ask_name]
            print(f"{ask_name} has been deleted")
        else:
            print(f"There is no data for name {ask_name}")
    
        self.main()


    def view_item(self):
        for name,grade in self.student_dicts.items():
            print(name ,":", grade)
            
        self.main()
############################################################################

jh = Information() #Object of the class is created. And this object has ability to access methods and variables of class.
