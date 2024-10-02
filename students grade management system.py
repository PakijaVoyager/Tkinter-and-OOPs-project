student_dicts = {}
def add_items(name,grade):
    student_dicts[name] = grade
    print(f"{name} with grade {grade} has been successfully added")

def update_item(name,grade):
    if name in student_dicts:
        student_dicts[name] = grade
        print(f"{name}'s grade has been updated")

def del_item(name):
    del student_dicts[name]
    print(f"{name} has been deleted")

def view_item():
    for name,grade in student_dicts.items():
        print(name ,":", grade)
    

while True:
    ask_usr = int(input("Enter \n1 : Add\n2 : Update\n3 : Delete\n4 : View\n5 : Exit\n:"))
    if ask_usr == 1:
        ask_name = input("Enter your name : ")
        ask_grade = int(input("Enter your grade : "))
        add_items(ask_name,ask_grade)
        # student_dicts[ask_name] = ask_grade
    
    elif ask_usr == 2:
        ask_name = input("Enter your name : ")
        ask_grade = int(input("Enter grade to update : "))
        if ask_name in student_dicts:
            update_item(ask_name,ask_grade)

        else:
            print(f"{ask_name} is not in the list")
    
    elif ask_usr == 3:
        ask_name = input("Enter your name : ")
        if ask_name in student_dicts:
            del_item(ask_name)
    
    elif ask_usr == 4:
        view_item()
    
    elif ask_usr == 5:
        break
    
    else:
        print(f"{ask_usr} not in the option")

print("Thank You :) ")
        