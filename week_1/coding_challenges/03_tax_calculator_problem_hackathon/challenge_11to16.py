'''
Tax Calculator Problem– Hackathon  
GlobalNext Solutions, a rapidly growing IT company, employs a diverse workforce ranging from entry
level developers to senior executives. The HR department wants to streamline the tax calculation 
process for employees under the New Tax Regime (2023). They’ve decided to build a tax calculation 
program that computes salaries, taxes, and net incomes while ensuring compliance with the latest 
tax laws. 
As a software developer in GlobalNext’s HR-Tech team, you are tasked with developing this program. 
The system should process employee salary details, validate inputs, calculate taxes, and generate 
detailed reports. 
The program should: 
1. Accept employee details, including monthly salary components. 
2. Calculate gross and taxable income according to the New Tax Regime (2023). 
3. Compute the tax payable using the appropriate tax Coding Challenges. 
4. Apply any applicable standard deductions and rebates. 
Generate reports detailing gross salary, taxable income, tax payable, and net salary.
'''

'''
Coding Challenge 11: Basic Input and Salary Calculation 
Objective: Capture employee details and calculate the gross salary. 
Tasks: 
• Accept the following inputs for an employee: 
o Name 
o EmpID 
o Basic Monthly Salary 
o Special Allowances (Monthly) 
o Bonus Percentage (Annual Bonus as % of Gross Salary) 
• Calculate: 
o Gross Monthly Salary = Basic Salary + Special Allowances 
o Annual Gross Salary = (Gross Monthly Salary × 12) + Bonus 
• Output: Display the employee details, gross monthly salary, and annual gross salary. 
'''


'''
Coding Challenge 12: Taxable Income Calculation 
Objective: Calculate taxable income after standard deductions. 
Tasks: 
• Deduct a Standard Deduction of ₹50,000 from the annual gross salary. 
• Compute the Taxable Income and display all intermediate calculations. 
Output: Display gross salary, standard deduction and taxable income.

'''

'''
Coding Challenge 13: Tax and Rebate Calculation 
Objective: Compute tax payable using the New Tax Regime (2023) sCoding Challenges. 
Tasks: 
1. Calculate tax based on the following sCoding Challenges: 
o ₹0 - ₹3,00,000: 0% 
o ₹3,00,001 - ₹6,00,000: 5% 
o ₹6,00,001 - ₹9,00,000: 10% 
o ₹9,00,001 - ₹12,00,000: 15% 
o ₹12,00,001 - ₹15,00,000: 20% 
o Above ₹15,00,000: 30% 
2. Apply Section 87A Rebate: 
o Taxable income ≤ ₹7,00,000 → 100% rebate (tax payable = ₹0). 
3. Add a 4% Health and Education Cess to the calculated tax. 
Output: Display a detailed tax breakdown, including sCoding Challenges, cess, and total tax payable. 
'''

'''
Coding Challenge 14: Net Salary Calculation 
Objective: Calculate annual net salary after tax deductions. 
Tasks: 
1. Compute Net Salary = Annual Gross Salary - Total Tax Payable. 
2. Display: 
o Annual Gross Salary 
o Total Tax Payable (including cess) 
o Annual Net Salar
'''


'''
Coding Challenge 15: Report Generation 
Objective: Generate a detailed report for employees. 
Tasks: 
1. Summarize all computed details: 
o Employee Details (Name, EmpID) 
o Gross Monthly Salary 
o Annual Gross Salary 
o Taxable Income 
o Tax Payable (with breakdown) 
o Annual Net Salary 
2. Format the output as a report for better readability. 
Output: 
• Provide a clean, tabular report for employees. 
Example Output (For Reports Level) 

Employee Tax Report 

Field    Details 
Name     John Doe 
EmpID    E12345 
Gross Monthly Salary ₹85,000

Annual Gross Salary ₹10,20,000 
Taxable Income      ₹9,70,000 
Tax Payable         ₹76,800 
Annual Net Salary   ₹9,43,200 
'''

'''
Coding Challenge 16: Input Validation Rules 
Objective: Validate all inputs to ensure accuracy and correctness. 
Validation Rules: 
1. Employee Details: 
o Name: Non-empty, alphabets only, max 50 characters. 
o EmpID: Alphanumeric, 5–10 characters. 
2. Salary Inputs: 
o Basic Salary: Positive number, max ₹1,00,00,000. 
o Special Allowances: Non-negative, max ₹1,00,00,000. 
o Bonus Percentage: Numeric value, 0–100. 
3. Derived Calculations: 
o Gross Monthly Salary must be greater than zero. 
o Annual Gross Salary should not exceed realistic values. 
4. General: 
o Reject invalid inputs with a clear error message. 
o Provide re-entry prompts for invalid data. 
Output: 
• Indicate if any inputs are invalid and prompt for correction.
'''

# -------------------------------------------------------------
# -------------------------------------------------------------


# Coding Challenge 11: Basic Input and Salary Calculation 

# Function to input employee details
def input_employee_details():
    
    # Coding Challenge 16: Input Validation Rules
    # Helper function for input validation
    def get_valid_input(prompt, input_type, validator, error_message):
        while True:
            try:
                user_input = input(prompt)
                value = input_type(user_input)
                if validator(value):
                    return value
                else:
                    print(f"Error: {error_message}")
            except ValueError:
                print(f"Error: Invalid input format. Please enter a valid {input_type.__name__}.")



    text = f"""
======================================================
                ENTER EMPLOYEE DETAILS
======================================================
    """
    print(f"\n{text}")

    # Name: Non-empty, alphabets only, max 50 characters.
    name = get_valid_input(
        "Enter Employee Name: ",
        str,
        lambda x: 0 < len(x) <= 50 and x.replace(" ", "").isalpha(),
        "Name must be non-empty, alphabets only (max 50 chars)."
    )

    # EmpID: Alphanumeric, 5–10 characters.
    emp_id = get_valid_input(
        "Enter Employee ID: ",
        str,
        lambda x: x.isalnum() and 5 <= len(x) <= 10,
        "EmpID must be alphanumeric and 5-10 characters."
    )

    # Basic Salary: Positive number, max ₹1,00,00,000.
    basic_salary = get_valid_input(
        "Enter Basic Monthly Salary: ",
        float,
        lambda x: 0 < x <= 10000000,
        "Basic Salary must be a positive number (max 1,00,00,000)."
    )

    # Special Allowances: Non-negative, max ₹1,00,00,000.
    special_allowances = get_valid_input(
        "Enter Special Allowances (Monthly): ",
        float,
        lambda x: 0 <= x <= 10000000,
        "Special Allowances must be non-negative (max 1,00,00,000)."
    )

    # Bonus Percentage: Numeric value, 0–100.
    bonus_percentage = get_valid_input(
        "Enter Bonus Percentage (Annual Bonus as % of Gross Salary): ",
        float,
        lambda x: 0 <= x <= 100,
        "Bonus Percentage must be between 0 and 100."
    )

    return {
        'name': name, 
        'emp_id': emp_id, 
        'basic_salary': basic_salary, 
        'special_allowances': special_allowances, 
        'bonus_percentage': bonus_percentage
        }

# Function to calculate gross salary
def calculate_gross_salary(basic_salary, special_allowances, bonus_percentage):
    gross_monthly_salary = basic_salary + special_allowances
    annual_bonus = (bonus_percentage / 100) * (gross_monthly_salary * 12)
    annual_gross_salary = (gross_monthly_salary * 12) + annual_bonus
    return gross_monthly_salary, annual_gross_salary

# Function to display employee salary details
def display_employee_salary_details(employee_details):
    text = f"""
======================================================
                EMPLOYEE SALARY DETAILS
======================================================
    """
    print(f"\n{text}")
    print(f"{'Name:':<30} {employee_details['name']}")
    print(f"{'Employee ID:':<30} {employee_details['emp_id']}")
    print(f"{'Gross Monthly Salary:':<30} ₹{employee_details['gross_monthly_salary']:,.2f}")
    print(f"{'Annual Gross Salary:':<30} ₹{employee_details['annual_gross_salary']:,.2f}")
 
# -------------------------------------------------------------
# -------------------------------------------------------------
   
# Coding Challenge 12: Taxable Income Calculation 

# Function to calculate and display taxable income
def calculate_and_display_taxable_income(annual_gross_salary):
    standard_deduction = 50000
    taxable_income = max(0, annual_gross_salary - standard_deduction)
    text = f"""
======================================================
                TAXABLE INCOME DETAILS
======================================================
    """
    print(f"\n{text}")
    print(f"{'Annual Gross Salary:':<30} ₹{annual_gross_salary:,.2f}")
    print(f"{'Standard Deduction:':<30} ₹{standard_deduction:,.2f}")
    print(f"{'Taxable Income:':<30} ₹{taxable_income:,.2f}\n")
    return taxable_income

# -------------------------------------------------------------
# -------------------------------------------------------------

# Coding Challenge 13: Tax and Rebate Calculation

# Function to calculate tax payable
def calculate_tax_payable(taxable_income):  
    if taxable_income < 0:
        raise ValueError("Taxable income cannot be negative")
    
    # Slabs as (lower_exclusive, upper_inclusive, rate) in rupees
    slabs = [
        (0,        300000, 0.00),
        (300000,   600000, 0.05),
        (600000,   900000, 0.10),
        (900000,  1200000, 0.15),
        (1200000, 1500000, 0.20),
        (1500000, float("inf"), 0.30),
    ]
    
    ramaining_income = taxable_income
    tax_by_slab = []
    total_tax = 0.0
    
    for lower, upper, rate in slabs:
        # taxable portion inside this slab:
        # slab_lower_exclusive -> slab applies from (lower+1) to upper but in continuous money terms we use max(0, min(taxable_income, upper) - lower)
        taxable_portion = max(0, min(taxable_income, upper) - lower)
        tax_for_slab = taxable_portion * rate
        tax_by_slab.append({
            "slab_range": f"₹{int(lower)+1:,} - ₹{int(upper):,}" if upper != float("inf") else f"₹{int(lower)+1:,} and above",
            "taxable_amount": int(taxable_portion),
            "rate_percent": int(rate * 100),
            "tax": round(tax_for_slab, 2)
        })
        
        total_tax += tax_for_slab
        
    # Apply Section 87A Rebate
    rebate_applied = False
    rebate_amount = 0.0
    
    if taxable_income <= 700000:
        rebate_amount = total_tax  # 100% rebate
        total_tax = 0.0
        rebate_applied = True
        
    # Add Health and Education Cess of 4% on tax after rebate
    cess = round(total_tax * 0.04, 2)
    total_tax_payable = round(total_tax + cess, 2)
    
    breakdown = {
        "taxable_income": int(taxable_income),
        "tax_by_slab": tax_by_slab,
        "tax_before_rebate": round(sum(item["tax"] for item in tax_by_slab), 2),
        "rebate_applied": rebate_applied,
        "rebate_amount": round(rebate_amount, 2),
        "tax_after_rebate": round(total_tax, 2),
        "cess_4_percent": cess,
        "total_tax_payable": total_tax_payable
    }
    
    return breakdown

# Function to display tax breakdown
def display_tax_breakdown(tax_breakdown):
    text = f"""
======================================================
                TAX BREAKDOWN
======================================================
    """
    print(f"\n{text}")
    print(f"Taxable Income: ₹{tax_breakdown['taxable_income']:,}\n")
    print("Breakdown by slab:")
    for item in tax_breakdown["tax_by_slab"]:
        slab = f"{item['slab_range']:<35}"                        # left aligned slab label
        taxable_amt = f"₹{item['taxable_amount']:>9,}"             # right aligned with grouping
        rate = f"{item['rate_percent']:2d}%"                       # percent
        tax = f"₹{item['tax']:>10,.2f}"                            # right aligned with 2 decimals
        print(f"  {slab} | Taxable: {taxable_amt} | Rate: {rate} | Tax: {tax}")
    print()
    print(f"{'Tax before rebate:':<30} ₹{tax_breakdown['tax_before_rebate']:,.2f}")
    if tax_breakdown.get("rebate_applied"):
        print(f"{'Section 87A rebate:':<30} -₹{tax_breakdown['rebate_amount']:,.2f}  (Full rebate applied since income ≤ ₹700,000)")
    else:
        print(f"{'Section 87A rebate:':<30} ₹0.00")
    print(f"{'Tax after rebate:':<30} ₹{tax_breakdown['tax_after_rebate']:,.2f}")
    print(f"{'Health & Education Cess (4%):':<30} ₹{tax_breakdown['cess_4_percent']:,.2f}")
    print(f"{'Total tax payable:':<30} ₹{tax_breakdown['total_tax_payable']:,.2f}")
    

# -------------------------------------------------------------
# -------------------------------------------------------------

# Coding Challenge 14: Net Salary Calculation

# Function to calculate net salary after tax deductions
def calculate_and_display_net_salary(annual_gross_salary, total_tax_payable):
    annual_net_salary = annual_gross_salary - total_tax_payable
    
    text = f"""
======================================================
                NET SALARY DETAILS
======================================================
    """
    print(f"\n{text}")
    print(f"{'Annual Gross Salary:':<35} ₹{annual_gross_salary:,.2f}")
    print(f"{'Total Tax Payable (including cess):':<35} ₹{total_tax_payable:,.2f}")
    print(f"{'Annual Net Salary:':<35} ₹{annual_net_salary:,.2f}")
    return annual_net_salary

# -------------------------------------------------------------
# -------------------------------------------------------------

# Coding Challenge 15: Report Generation

def generate_and_print_detailed_report(employee_details, taxable_income, total_tax_payable, annual_net_salary):
    
    # Fixed column widths
    field_width = 24
    value_width = 28

    def row(field, value):
        return f"| {field:<{field_width}} | {value:<{value_width}} |"

    table = f"""
======================================================
                 EMPLOYEE TAX REPORT
======================================================

+--------------------------+------------------------------+
{row("Name", employee_details['name'])}
{row("EmpID", employee_details['emp_id'])}
{row("Gross Monthly Salary", f'₹{employee_details["gross_monthly_salary"]:,.0f}')}
{row("Annual Gross Salary", f'₹{employee_details["annual_gross_salary"]:,.0f}')}
{row("Taxable Income", f'₹{taxable_income:,.0f}')}
{row("Tax Payable", f'₹{total_tax_payable:,.0f}')}
{row("Annual Net Salary", f'₹{annual_net_salary:,.0f}')}
+--------------------------+------------------------------+

"""
    print(table)



# -------------------------------------------------------------
# -------------------------------------------------------------

# Coding Challenge 16: Input Validation Rules 
# Input validation is integrated into the input_employee_details function


# -------------------------------------------------------------
# -------------------------------------------------------------


# Main function to execute the program
if __name__ == "__main__":
    
    
# Coding Challenge 11: Basic Input and Salary Calculation 

    employee_details = input_employee_details()
    gross_monthly_salary, annual_gross_salary = calculate_gross_salary(
        employee_details['basic_salary'],
        employee_details['special_allowances'],
        employee_details['bonus_percentage']
    )
    employee_details.update({
        'gross_monthly_salary': gross_monthly_salary,
        'annual_gross_salary': annual_gross_salary
    })
    display_employee_salary_details(employee_details) 
    
    

 # Coding Challenge 12: Taxable Income Calculation  
 
    taxable_income = calculate_and_display_taxable_income(annual_gross_salary)
    
# Coding Challenge 13: Tax and Rebate Calculation

    tax_breakdown = calculate_tax_payable(taxable_income)
    display_tax_breakdown(tax_breakdown)
    
# Coding Challenge 14: Net Salary Calculation

    annual_net_salary = calculate_and_display_net_salary(annual_gross_salary, tax_breakdown['total_tax_payable'])
    
# Coding Challenge 15: Report Generation

    generate_and_print_detailed_report(employee_details, taxable_income, tax_breakdown['total_tax_payable'], annual_net_salary)

# Coding Challenge 16: Input Validation Rules
# Input validation is integrated into the input_employee_details function
