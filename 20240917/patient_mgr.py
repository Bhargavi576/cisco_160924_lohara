class Patient:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def __str__(self):
        return f'[id={self.id}, name={self.name}]'
    def __repr__(self):
        return self.__str__()
patients=[]
def patient_add(id,name):
    global patients
    patient=Patient(id,name)
    patients.append(patient)
def patient_remove(id):
    global patients
    for patient in patients:
        if patient.id==id:
            print(patient)
            if input('are you sute to delete(yes/no)').lower() =='yes':
                patients.remove(patient)
                print('patinet deleted successfully')
            return
    print(f'no such id{id}')
def patient_display():
    global patients
    for patient in patients:
        print(patient)
def menu():
    choice=int(input('''1.add patient
    2.delete patient
    3.display patient list
    4.end'''))
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
        pass
    else:
        print('invalid menu')
    
def menus():
    choice=menu()
    while choice !=4:
        choice=menu()
    print('Thankyou for using the app')

menus()




