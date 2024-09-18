from patient_service import patient_add,patient_display,patient_display_by_id
from patient_service import patient_update,patient_remove
def menu():
    choice=int(input('''1.add patient
    2.delete patient
    3.display patient list
    4.display patient by id
    5.update patinet by id
    7.end'''))
    if choice==1:
        id=int(input("enter patient id"))
        name=input("enter patient name")
        patient_add(id,name)
    elif choice==2:
        id=int(input("enter patient id to remove"))
        patient_remove(id)
    elif choice==3:
        patient_display()
    elif choice==4:
        id=int(input("enter patient id"))
        patient_display_by_id(id)
    elif choice==5:
        id=int(input("enter patient id"))
        patient_update(id)
    elif choice==7:
        pass
    else:
        print('invalid menu')
    return choice
    
def menus():
    choice=menu()
    while choice !=7:
        choice=menu()
    print('Thankyou for using the app')

menus()