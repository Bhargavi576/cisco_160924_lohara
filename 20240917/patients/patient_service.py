from Patient import Patient
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
def patient_update(id):
    global patients
    for patient in patients:
        if patient.id==id:
            patient.name=input(f'enter new name({patient.name})')
            print('patient updated successfully')
        return
    print(f'no such id{id}')
    
def patient_display():
    global patients
    for patient in patients:
        print(patient)
def patient_display_by_id(id):
    global patients
    for patient in patients:
        if patient.id==id:
            print(patient)
            return