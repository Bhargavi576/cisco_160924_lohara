patients=[]
def add_patients(name):
    patients.append(name)
    print("The patient {} is added successfully".format(name))

def delete_patients(name):
    if name in patients:
        patients.remove(name)
        print("The patient {} is removed".format(name))

def display_patients():
    if patients:
        print("The current patients list")
        print(patients)
    else:
        print("no patients in the list")

add_patients('siri')
add_patients('sari')
add_patients('deepu')

delete_patients('deepu')
delete_patients('leela')

display_patients()

