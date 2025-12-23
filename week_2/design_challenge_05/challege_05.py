'''
Design Challenge 5: Hospitals and Surgeons Management 
There is a surgeon management system where a surgeon works for many hospitals and conducts  
operation on patients admitted in a ward. The surgeon are of various type such as Senior, Non-senior 
,etc. 
Design the OO model for the above problem statement and implement the code to 
• Total number of patient being operated 
• List all the patient being operated by a surgeon 
• List all the patient admitted to a ward.
'''


class Patient:
    def __init__(self, patient_id, name):
        self.__patient_id = patient_id
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def patient_id(self):
        return self.__patient_id

    def __str__(self):
        return f"{self.__patient_id} - {self.__name}"


class Ward:
    def __init__(self, ward_name):
        self.__ward_name = ward_name
        self.__patients = []   # composition

    @property
    def ward_name(self):
        return self.__ward_name

    def admit_patient(self, patient):
        self.__patients.append(patient)

    def list_patients(self):
        return self.__patients


class Hospital:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Surgeon:
    def __init__(self, surgeon_id, name, surgeon_type):
        self.__surgeon_id = surgeon_id
        self.__name = name
        self.__surgeon_type = surgeon_type   # Senior / Non-Senior
        self.__hospitals = []
        self.__operations = []

    @property
    def name(self):
        return self.__name

    def assign_hospital(self, hospital):
        self.__hospitals.append(hospital)

    def perform_operation(self, operation):
        self.__operations.append(operation)

    def list_operated_patients(self):
        return [op.patient for op in self.__operations]

    def __str__(self):
        return f"{self.__surgeon_id} - {self.__name} ({self.__surgeon_type})"


class Operation:
    def __init__(self, surgeon, patient, ward):
        self.__surgeon = surgeon
        self.__patient = patient
        self.__ward = ward

    @property
    def surgeon(self):
        return self.__surgeon

    @property
    def patient(self):
        return self.__patient

    @property
    def ward(self):
        return self.__ward


class SurgeonManagementSystem:
    def __init__(self):
        self.__operations = []

    def add_operation(self, operation):
        self.__operations.append(operation)
        operation.surgeon.perform_operation(operation)

    # 1. Total number of patients being operated
    def total_patients_operated(self):
        return len(self.__operations)

if __name__ == "__main__":
    # Hospitals
    h1 = Hospital("City Hospital")
    h2 = Hospital("Care Plus")

    # Wards
    ward_icu = Ward("ICU")
    ward_general = Ward("General")

    # Patients
    p1 = Patient(1, "Ramesh")
    p2 = Patient(2, "Suresh")
    p3 = Patient(3, "Anita")

    # Admit patients to wards
    ward_icu.admit_patient(p1)
    ward_icu.admit_patient(p2)
    ward_general.admit_patient(p3)

    # Surgeons
    s1 = Surgeon(101, "Dr. Sharma", "Senior")
    s2 = Surgeon(102, "Dr. Mehta", "Non-Senior")

    # Assign hospitals
    s1.assign_hospital(h1)
    s1.assign_hospital(h2)
    s2.assign_hospital(h1)

    # Management system
    system = SurgeonManagementSystem()

    # Operations
    op1 = Operation(s1, p1, ward_icu)
    op2 = Operation(s1, p2, ward_icu)
    op3 = Operation(s2, p3, ward_general)

    system.add_operation(op1)
    system.add_operation(op2)
    system.add_operation(op3)

    # -------------------------
    # Required Outputs
    # -------------------------

    # 1. Total number of patients being operated
    print("Total patients operated:", system.total_patients_operated())

    # 2. List all patients operated by a surgeon
    print("\nPatients operated by", s1.name)
    for patient in s1.list_operated_patients():
        print(patient)

    # 3. List all patients admitted to a ward
    print("\nPatients admitted to ward:", ward_icu.ward_name)
    for patient in ward_icu.list_patients():
        print(patient)
