'''
Setting the Scene: A Day at HealWell Care Hospital 
At HealWell Care Hospital, the day begins with the admin team preparing the system for patient 
care. The admin updates the list of services available for the day, ensuring accuracy and clarity. These 
services include a mix of diagnostics and consultations: 
• General Consultation 
• Blood Test 
• Covid Test 
• X-Ray 
• CT Scan 
• MRI 
Once the services are set, the hospital welcomes patients who require seamless and efficient billing 
processes. The objective is to build a robust system where patient information, service selection, 
billing, and tax calculations are handled smoothly while keeping the user experience intuitive and 
error-free. 
Consider these 2 arrays (Declare them initially) 
Services: ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]   
Costs: [500, 300, 800, 1500, 4000, 7000]   
Requirements & Levels 


Level 1: Patient Walks In and Shares Their Details 
Patients like Mr. Arjun Kumar visit the hospital. At the reception, their basic details (name, age, 
contact, and gender) are collected and stored in variables. 
Example Input: 
Name: Arjun Kumar   
Age: 35   
Gender: Male   
Contact: 9876543210   


Level 2: Displaying Services for Patient Selection 
The system displays the list of services available for the day. The patient selects one or more services 
they wish to avail. The selected services are stored in an array (selected_services). 
Example Interaction: 
Available Services:   
1. General Consultation   
2. Blood Test   
3. Covid Test   
4. X-Ray   
5. CT Scan   
6. MRI   
Patient Selected: [1, 4]  // General Consultation, X-Ray   
Selected Services Array: ["General Consultation", "X-Ray"]   


Level 3: Fetching Costs of Selected Services 
The system iterates through the selected_services array, matches the services with the main services 
array, and retrieves the respective costs from the costs array. 
Example Output: 
Selected Services: ["General Consultation", "X-Ray"]   
Selected Costs: [500, 1500]   


Level 4: Calculating the Total Cost 
The total cost is calculated by summing up the costs of all selected services. 
Example Output: 
Total Cost (Before Tax): ₹2000   


Level 5: Applying GST to the Bill 
An 18% GST is applied to the total cost. The system calculates and adds this to the total bill amount. 
Example Output: 
GST (18%): ₹360   
Grand Total: ₹2360

   
Level 6: Generating and Displaying the Invoice 
The system generates a detailed invoice for the patient, including their details, services availed, 
individual costs, and the grand total. 
Example Output: ----------------------------------------------- 
HealWell Care Hospital   
Patient Invoice   -----------------------------------------------   
 
Patient Information:   
Name: Arjun Kumar   
Age: 35   
Gender: Male   
Contact: 9876543210   
 
Services Availed:   
1. General Consultation: ₹500   
2. X-Ray: ₹1500   
 
Subtotal: ₹2000   
GST (18%): ₹360   
Grand Total: ₹2360   
 
Thank you for choosing HealWell Care Hospital!   


----------------------------------------------- 

Level 7: Setting Up the Services of the Day (Admin Task) 
The admin prepares the hospital system by entering the available services into the system. Hospital 
wants the flexibility to configure the services. This list is stored in an array. Each service has a name, 
and its corresponding cost is stored in a separate array for flexibility. 
• Array 1: Stores the names of services (services array). 
• Array 2: Stores the costs of the services (costs array). 
Example Input: 
Services: ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]   
Costs: [500, 300, 800, 1500, 4000, 7000]   
Objective: Ensure services and costs are paired for seamless retrieval. 


Level 8: Providing Discounts (Optional Enhancements) 
Context 
HealWell Care Hospital values its patients and strives to provide the best care at affordable rates. To 
improve accessibility and express gratitude, the hospital offers discounts in specific scenarios. 
Discount Rules 
1. Senior Citizen Discount: 
Patients aged 60 or above are eligible for a 10% discount on the subtotal (before GST). 
2. High-Bill Discount: 
If the subtotal exceeds ₹5000, an additional 5% discount is applied on the subtotal (after any 
other discounts). 
Steps 
1. Check the patient's age to determine if the senior citizen discount applies. 
2. Check the subtotal to determine if the high-bill discount applies. 
3. Calculate the final total after applying discounts and GST.
 
'''


# Level 1: Patient Walks In and Shares Their Details

# Function to input name
def input_name():
    while True:
        name = input("\nEnter Patient Name: ").strip()
        if name:
            return name
        else:
            print("Name cannot be empty. Please enter a valid name.")
            
# Function to input age
def input_age():
    while True:
        try:
            age = int(input("Enter Patient Age: "))
            if age <= 0:
                print("Please enter a positive integer greater than 0.")
                continue
            return age
        except ValueError:
            print("Invalid input. Please enter a valid positive integer for age.")

# Function to input gender,age
def input_gender():
    while True:
        try:
            gender = input("Enter Patient Gender: ").strip()
            if not gender:
                print("Gender cannot be empty. Please enter a valid gender.")
                continue        
            return gender
        except ValueError:
            print("Invalid input. Please enter a valid gender.")
            
# Function to input contact number
def input_contact():
    while True:
        try:
            contact = input("Enter Patient Contact Number: ").strip()
            if not contact.isdigit() or len(contact) != 10:
                print("Invalid contact number. Please enter a 10-digit number.")
                continue        
            return contact
        except ValueError:
            print("Invalid input. Please enter a valid contact number.")
            

# Function to collect patient details
def collect_patient_details():  
    name = input_name()
    age = input_age()
    gender = input_gender()
    contact = input_contact()  
    return {
        "name": name,
        "age": age,
        "gender": gender,
        "contact": contact
    }
    
# Function to display patient details
def display_patient_details(details):
    print(f"\nPatient Details :\n")
    print(f"{'Name:':<15} {details['name']}")
    print(f"{'Age:':<15} {details['age']}") 
    print(f"{'Gender:':<15} {details['gender']}")
    print(f"{'Contact:':<15} {details['contact']}")
    print()
    
    
# Level 2: Displaying Services for Patient Selection

# Function to display the services
def display_services(services):
    print("-" * 30)
    print(f"Available Services :\n")
    print(f"{'No.':<5} {'Service Name'}") 
    print("-" * 30)
    for idx, service in enumerate(services, start=1):
        print(f"{idx:<5} {service}")
    print("-" * 30)
        
# Function to select services
def select_services(services):
    selected_services = []
    while True:
        try:
            selections = input("\nEnter the numbers of the services you want to select (comma-separated): ")
            indices = [int(i.strip()) for i in selections.split(",")]
            for index in indices:
                if 1 <= index <= len(services):
                    selected_services.append(services[index - 1])
                else:
                    print(f"Service number {index} is out of range. Please select valid service numbers.")
                    selected_services = []
                    break
            if selected_services:
                break
        except ValueError:
            print("Invalid input. Please enter valid service numbers.")
    return selected_services

# Function to display selected services
def display_selected_services(selected_services,selected_costs,message=f"\nSelected Services :\n"):
    print(message)
    for service, cost in zip(selected_services, selected_costs):
        print(f"{service:<25} : ₹{cost:>8.2f}")
    print()
        
# Level 3: Fetching Costs of Selected Services

# Function to fetch costs of selected services
def fetch_selected_costs(selected_services, services, costs):
    selected_costs = []
    for service in selected_services:
        if service in services:
            index = services.index(service)
            selected_costs.append(costs[index])
    return selected_costs

# Level 4: Calculating the Total Cost

# Function to calculate total cost
def calculate_total_cost(selected_costs):
    return sum(selected_costs)

# Function to display subtotal
def display_subtotal(subtotal, message="Subtotal "):
    print(f"{message:<25} : ₹{subtotal:>8.2f}")

    
# Level 5: Applying GST to the Bill

# Function to calculate GST and grand total
def calculate_gst_and_grand_total(total_cost):
    gst = total_cost * 0.18
    grand_total = total_cost + gst
    return gst, grand_total

# Function to display GST and grand total
def display_gst_and_grand_total(gst, grand_total):
    print(f"{'GST (18%)':<25} : ₹{gst:>8.2f}")
    print(f"{'Grand Total':<25} : ₹{grand_total:>8.2f}")
    
# Level 6: Generating and Displaying the Invoice 

# Function to generate and display invoice
def generate_and_display_invoice(patient_details, selected_services, selected_costs, subtotal, discount, gst, grand_total):
    print("\n" + "="*50)
    print(f"{'HealWell Care Hospital':^50}")
    print(f"{'Patient Invoice':^50}")
    print("="*50)
    
    display_patient_details(patient_details)
    
    print("-"*50)
    display_selected_services(selected_services, selected_costs, "Services Availed :\n")
    print("-" * 50)
    
    display_subtotal(subtotal)
    if discount > 0:
        display_discount(discount)
    display_gst_and_grand_total(gst, grand_total)
    
    print(f"\n{'Thank you for choosing HealWell Care Hospital!':^50}")
    print("=" * 50)
    
# Level 7: Setting Up the Services of the Day (Admin Task) 

# Function to set up services and costs
def setup_services_and_costs():
    services = []
    costs = []
    print("\nAdmin: Set Up Services for the Day")
    while True:
        service = input("\nEnter service name (or type 'done' to finish): ").strip()
        if service.lower() == 'done':
            break
        while True:
            try:
                cost = float(input(f"Enter cost for {service}: "))
                if cost < 0:
                    print("Cost cannot be negative. Please enter a valid cost.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid cost.")
        services.append(service)
        costs.append(cost)
    return services, costs

# Level 8: Providing Discounts (Optional Enhancements)

# Function to apply discounts
def apply_discounts(total_cost, age):
    discount = 0
    # Senior Citizen Discount
    if age >= 60:
        discount += total_cost * 0.10
    # High-Bill Discount
    if total_cost > 5000:
        discount += (total_cost - discount) * 0.05
        
    total_cost -= discount
    return discount, total_cost

# Function to display discount
def display_discount(discount):
    print(f"{'Discount':<25} : -₹{discount:>8.2f}")
    
# Function to display discount and total cost
def display_discount_and_total_cost(discount,total_cost):
    print(f"{'Discount':<25} : -₹{discount:>8.2f}")
    print(f"{'Total Cost After Discount':<25} : ₹{total_cost:>8.2f}")


# Main block to execute the program
if __name__ == "__main__":
    
    services = ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]   
    costs = [500, 300, 800, 1500, 4000, 7000]   
    
    # Level 7: Setting Up the Services of the Day (Admin Task) 
    #services, costs = setup_services_and_costs()
    
    # Level 1: Patient Walks In and Shares Their Details
    patient_details = collect_patient_details()
    display_patient_details(patient_details)
    
    # Level 2: Displaying Services for Patient Selection
    display_services(services)
    selected_services = select_services(services)
    
    
    # Level 3: Fetching Costs of Selected Services
    selected_costs = fetch_selected_costs(selected_services, services, costs)
    
    display_selected_services(selected_services,selected_costs)
    
    # Level 4: Calculating the Total Cost
    subtotal = calculate_total_cost(selected_costs)
    display_subtotal(subtotal)
    
    # Level 8: Providing Discounts (Optional Enhancements)
    discount, total_cost_after_discount = apply_discounts(subtotal, patient_details['age'])
    display_discount_and_total_cost(discount, total_cost_after_discount)
    
    # Level 5: Applying GST to the Bill
    gst, grand_total = calculate_gst_and_grand_total(total_cost_after_discount)
    display_gst_and_grand_total(gst, grand_total)
    
    # Level 6: Generating and Displaying the Invoice 
    generate_and_display_invoice(patient_details, selected_services, selected_costs, subtotal, discount, gst, grand_total)
    
    

    
    
    
    
    
    
    