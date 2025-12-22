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
        self.patient_id = patient_id
        self.name = name

    def __str__(self):
        return f"{self.patient_id} - {self.name}"


class Ward:
    def __init__(self, ward_name):
        self.ward_name = ward_name
        self.patients = []   # composition

    def admit_patient(self, patient):
        self.patients.append(patient)

    def list_patients(self):
        return self.patients


class Hospital:
    def __init__(self, name):
        self.name = name


class Surgeon:
    def __init__(self, surgeon_id, name, surgeon_type):
        self.surgeon_id = surgeon_id
        self.name = name
        self.surgeon_type = surgeon_type   # Senior / Non-Senior
        self.hospitals = []
        self.operations = []

    def assign_hospital(self, hospital):
        self.hospitals.append(hospital)

    def perform_operation(self, operation):
        self.operations.append(operation)

    def list_operated_patients(self):
        return [op.patient for op in self.operations]

    def __str__(self):
        return f"{self.surgeon_id} - {self.name} ({self.surgeon_type})"


class Operation:
    def __init__(self, surgeon, patient, ward):
        self.surgeon = surgeon
        self.patient = patient
        self.ward = ward


class SurgeonManagementSystem:
    def __init__(self):
        self.operations = []

    def add_operation(self, operation):
        self.operations.append(operation)
        operation.surgeon.perform_operation(operation)

    # 1. Total number of patients being operated
    def total_patients_operated(self):
        return len(self.operations)

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
