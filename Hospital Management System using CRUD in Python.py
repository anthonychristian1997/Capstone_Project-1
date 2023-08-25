
# import random ( Generate random patient ID )
from random import randint

# Define the patient data collection
DATA_PASIEN = {} # Dictionary
TRASH_CAN = {}
DATA_USER = {
    "admin": {
        "username": "admin",
        "password": "admin"
    }
}
choice = 0

def my_function():
    pass

# Define Patient ID
def generate_patient_id():
    """Generate new patient ID"""

    id_exist = True

    while id_exist:
        # random_number = random.randint(0, 999)
        random_number = randint(0, 999) # generate random number

        if random_number < 10: # satuan
            generated_id = "P" + "000" + str(random_number)
        elif random_number < 100: # puluhan
            generated_id = "P" + "00" + str(random_number)
        elif random_number < 1000: # ratusan
            generated_id = "P" + "0" + str(random_number)

        if generated_id in DATA_PASIEN:
            id_exist = True
        else:
            id_exist = False

    return generated_id

# Create Delete Function
def delete_patient():

    read_patient()

    input_check = True
    while input_check:
        try:
            id_input = input("Input ID to be removed: ")
        except:
            print("Please input ID...")
        
        if id_input in DATA_PASIEN:
            input_check = False
        else:
            input_check = True

    # Pindahkan ke "tong sampah"

    TRASH_CAN.update(DATA_PASIEN[id_input])

    # print(f"Trash can: {TRASH_CAN}")
    # DATA_PASIEN.UPDATE(TRASH_CAN[id_input])

    DATA_PASIEN.pop(id_input)

    input("Data has been deleted... Press [Enter to continue]")
    
# Create Update Function
def update_patient():

    read_patient()
    id_input = input("Input ID to be updated: ")

    patient_name = ''
    number_check = False
    while (len(patient_name) < 5 or len(patient_name) > 15) or number_check == True:
        try:
            patient_name = input("Please enter the patient's name [3-15 digits]: ")
        except:
            print("Please input the patient's name..")
            patient_name = ''
            input()

        # Return True if there's number in name
        number_check = any(digit.isdigit() for digit in patient_name) 

    patient_disease = ''
    while len(patient_disease) < 3:
        try:
            patient_disease = input(f"Please enter the {patient_name}'s disease [Min. 3 digit]: ")
        except:
            print("Please input the patient's name..")
            patient_disease = ''
            input()

    patient_room_type = ''
    while patient_room_type != "Kelas III" and patient_room_type != "Kelas II" and patient_room_type != "Kelas I" and patient_room_type != "VIP":
        try:
            patient_room_type = input(f"Please enter the {patient_name}'s room type [Kelas III | Kelas II | Kelas I | VIP]: ")
        except:
            print("Please input the patient's room type..")
            patient_room_type = ''
            input()
    
    patient_stay_duration = 0
    while patient_stay_duration < 1:
        patient_stay_duration = int(input(f"Please enter the {patient_name}'s length of stay [in days]: "))
    
    patient_doctor = ''
    number_check = False
    while (len(patient_doctor) < 5 or len(patient_doctor) > 15) or number_check == True:
        try:
            patient_doctor = input("Please enter the patient's doctor [3-15 digits]: ")
        except:
            print("Please input the patient's doctor..")
            patient_doctor = ''
            input()
        
        # Return True if there's number in name
        number_check = any(digit.isdigit() for digit in patient_doctor) 
    
    doctor_name_formatted = "dr. " + patient_doctor
    
    DATA_PASIEN[id_input]["name"] = patient_name
    DATA_PASIEN[id_input]["disease"] = patient_disease
    DATA_PASIEN[id_input]["room_type"] = patient_room_type
    DATA_PASIEN[id_input]["stay_duration"] = patient_stay_duration
    DATA_PASIEN[id_input]["doctor_responsible"] = doctor_name_formatted

# Create Read Function
def read_patient():
    """show the current patient list"""
    
    clear_screen()
    # print(DATA_PASIEN)
    
    if len(DATA_PASIEN) == 0:
        print("There is no patient data...")
        input()
        return
    
    print("=======================================================================================================================")
    print("|    ID     |        Nama         |       Penyakit      |     Jenis Kamar    |     Durasi Inap    |       Dokter      |")
    print("=======================================================================================================================")
    
    for every_patient in DATA_PASIEN:
        print(f"| {DATA_PASIEN[every_patient]['ID']}  | {DATA_PASIEN[every_patient]['name']} | {DATA_PASIEN[every_patient]['disease']} | {DATA_PASIEN[every_patient]['room_type']} | {DATA_PASIEN[every_patient]['stay_duration']} hari | {DATA_PASIEN[every_patient]['doctor_responsible']} |")
    
    input("Press enter to continue...")

# Create Function to Add Patient Data
def create_patient():
    """Create new patient data"""
    
    patient_name = ''
    number_check = False
    while (len(patient_name) < 5 or len(patient_name) > 15) or number_check == True:
        try:
            patient_name = input("Please enter the patient's name [3-15 digits]: ")
        except:
            print("Please input the patient's name..")
            patient_name = ''
            input()
        
        # Return True if there's number in name
        number_check = any(digit.isdigit() for digit in patient_name) 
    
    patient_disease = ''
    while len(patient_disease) < 3:
        try:
            patient_disease = input(f"Please enter {patient_name}'s disease [Min. 3 digit]: ")
        except:
            print("Please input the patient's name..")
            patient_disease = ''
            input()
    
    patient_room_type = ''
    while patient_room_type != "Kelas III" and patient_room_type != "Kelas II" and patient_room_type != "Kelas I" and patient_room_type != "VIP":
        try:
            patient_room_type = input(f"Please enter {patient_name}'s room type [Kelas III | Kelas II | Kelas I | VIP]: ")
        except:
            print("Please input the patient's room type..")
            patient_room_type = ''
            input()
    
    patient_stay_duration = 0
    while patient_stay_duration < 1:
        patient_stay_duration = int(input(f"Please enter {patient_name}'s length of stay [in days]: "))
    
    patient_doctor = ''
    number_check = False
    while (len(patient_doctor) < 5 or len(patient_doctor) > 15) or number_check == True:
        try:
            patient_doctor = input("Please enter the patient's doctor [3-15 digits]: ")
        except:
            print("Please input the patient's doctor..")
            patient_doctor = ''
            input()
        
        # Return True if there's number in name
        number_check = any(character.isdigit() for character in patient_doctor) 
    
    doctor_name_formatted = "dr. " + patient_doctor
    
    patient_id = generate_patient_id()
    
    new_patient = {
        patient_id: {
            "ID": patient_id,
            "name": patient_name,
            "disease": patient_disease,
            "room_type": patient_room_type,
            "stay_duration": patient_stay_duration,
            "doctor_responsible": doctor_name_formatted
        }
    }
    
    DATA_PASIEN.update(new_patient)

# Create Home Screen & Clear Screen
def clear_screen():
    """Untuk membersihkan layar dari tampilan sebelumnya"""
    
    for i in range(10):
        print()


def home_screen():
    """
    Home screen display
    and returns the selected menu option
    
    """
    
    clear_screen()
    
    print(
        """
Hospital Data Patient RS. Purwadhika
=======================
1. Input New Patient Information
2. Show Patient Information
3. Change Patient Information
4. Delete Patient Information
5. Log-Out

Choose [1-5]: >> """, end=''
    )
    
    try:
        choice = int(input())
    except:
        input("Input must be an integer. Press [Enter] to continue...")
        choice = 0
    
    return choice

# Create login function
def login():
    not_logged_in = True
    while not_logged_in:
        input_username = input("Input username: ")
        input_password = input("Imput password: ")
        
        for every_user in DATA_USER:
            if input_username == DATA_USER[every_user]["username"]:
                if input_password == DATA_USER[every_user]["password"]:
                    not_logged_in = False

# Create main program
def main_program():
    choice = 0
    while choice != 5:
        choice = home_screen()
        
        if choice == 1:
            create_patient()
        elif choice == 2:
            read_patient()
        elif choice == 3:
            update_patient()
        elif choice == 4:
            delete_patient()


if __name__ == "__main__":
    
    login()
    
    main_program()

    my_function()
    
    input("Thank you for using this program... Press [Enter] to continue...")