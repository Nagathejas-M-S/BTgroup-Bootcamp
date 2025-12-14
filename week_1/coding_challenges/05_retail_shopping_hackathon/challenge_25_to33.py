'''
Retail Shopping– Hackathon  
Retail Shopping Application with Enhanced Rules 
You are tasked with developing a retail shopping application for generating itemized invoices, 
applying business rules for discounts, surcharges, and quantities, and providing a seamless customer 
experience. The application unfolds across levels, each introducing new functionality, culminating in 
a complete solution that includes invoice generation and a breakdown of purchases. 
'''


'''
Coding Challenge 25: Basic Item Entry and Total Calculation 
Objective: Allow the user to input item details (code, description, quantity, price) and calculate the 
total cost for the item. 
Key Steps: 
1. Accept item code, description, quantity, and price. 
2. Compute the total for a single item. 
3. Display the total for the item. 
'''

'''
Coding Challenge 26: Iterative Item Entry and Grand Total 
Objective: Enable multiple items to be added iteratively, and compute the grand total for all items. 
Key Steps: 
1. Use a loop to accept details for multiple items. 
2. Compute the grand total by summing individual totals. 
3. Display the grand total after all items have been entered. 

'''

'''
Coding Challenge 27: Applying Discounts 
Objective: Introduce business rules for modifying the grand total based on conditions. 
Rules Implemented: 
1. Discount: If the grand total exceeds ₹10,000, apply a 10% discount. 
2. Quantity Discount: If the total quantity exceeds 20, apply an additional 5% discount on the 
grand total (after other discounts). 
Key Steps: 
1. Check conditions for discounts. 
2. Adjust the grand total accordingly. 
3. Display the modified total with adjustments explained. 
'''

'''
Coding Challenge 28: Membership Discounts 
Objective: Introduce a membership system where customers get an additional discount. 
Rules Implemented: 
1. If the customer is a member (choice: 'y'), apply an additional 2% discount on the grand total 
after all other adjustments. 
Key Steps: 
1. Prompt the user for membership status. 
2. Apply the membership discount if applicable. 
3. Update and display the final grand total. 
SkillAssure HandsOn Framework - SAHF 
Inspiring excellence
'''

'''
Coding Challenge 29: Tax Calculation Based on Purchase Amount 
Objective: Introduce tiered tax rates based on the grand total. 
Rules Implemented 
1. If the grand total is below ₹5,000, apply 5% tax. 
2. If the grand total is between ₹5,000 and ₹20,000, apply 10% tax. 
3. If the grand total exceeds ₹20,000, apply 15% tax. 
Key Steps 
1. Calculate the tax based on the applicable tier. 
2. Add the tax to the grand total. 
3. Display the tax amount and updated grand total. 
'''

'''
Coding Challenge 30: Promotional Discounts on Specific Items 
Objective: Introduce promotional discounts on specific items identified by their code. 
Rules Implemented 
1. If the item code matches a promotional code (e.g., PROMO10), apply a 10% discount on that 
item. 
2. Compute the grand total considering the discounts on applicable items. 
Key Steps 
1. Check if the item code matches the promotional code. 
2. Apply the discount to the item total. 
3. Update the grand total and display the final value. 
'''

'''
Coding Challenge 31: Payment Mode Rules 
Objective: Incorporate business rules based on the selected payment method. 
Rules Implemented 
1. If the customer chooses Cash, no surcharge applies. 
2. If the customer chooses Credit Card, apply a flat 2% surcharge on the final grand total after 
all adjustments. 
Key Steps 
1. Prompt the user to select the payment method. 
2. Apply the surcharge if the method is Credit Card. 
3. Display the payment method, surcharge amount, and final payable amount. 
'''

'''
Coding Challenge 32: Minimum Purchase Requirements 
Objective 
Add a condition to enforce a minimum purchase value to generate an invoice. 
Rules Implemented 
1. If the final grand total (after discounts and taxes) is below ₹500, inform the user that the 
minimum purchase amount is not met. 
Key Steps 
1. Check the final grand total. 
2. If below ₹500, display an appropriate message and terminate the process. 
3. Otherwise, proceed to generate the invoice. 
SkillAssure HandsOn Framework - SAHF 
Inspiring excellence
'''

'''
Coding Challenge 33: Loyalty Points 
Objective: Introduce a loyalty program where customers earn points based on the final grand total. 
Rules Implemented 
1. For every ₹100 spent, the customer earns 1 loyalty point. 
2. Display the total loyalty points earned. 
Key Steps 
1. Calculate loyalty points (points = grand_total // 100). 
2. Display the earned points along with the invoice. 
'''


# -------------------------------------------------------------
# -------------------------------------------------------------


# Coding Challenge 25:  Basic Item Entry and Total Calculation 

# Function to take user input for item details
def user_input_item():
    item_code = input("\nEnter item code: ")
    item_description = input("Enter item description: ")
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please enter a valid quantity.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for quantity.")
    while True:
        try:
            price = float(input("Enter price per item: "))
            if price < 0:
                print("Price cannot be negative. Please enter a valid price.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for price.")
    return {
        "item_code": item_code, 
        "item_description": item_description, 
        "quantity": quantity, 
        "price": price
    }

# Function to compute total cost for the item
def compute_total(quantity, price):
    return quantity * price

# Function to display the total cost
def display_total(item):
    print(f"Total Cost for the Item: {item['total_cost']}")
    
# def display_item(item):
#     print(f"Item Code: {item['item_code']}")
#     print(f"Item Description: {item['item_description']}")
#     print(f"Quantity: {item['quantity']}")
#     print(f"Price per Item: {item['price']}")
#     print(f"Total Cost for the Item: {item['total_cost']}")
    

# -------------------------------------------------------------
# -------------------------------------------------------------

    
# Coding Challenge 26: Iterative Item Entry and Grand Total 

def iterative_item_entry():
    items = []
    grand_total = 0.0
    total_quantity = 0
    while True:
        item = user_input_item()
        total_cost = compute_total(item["quantity"], item["price"])
        item.update({"total_cost": total_cost})
        items.append(item)
        total_quantity += item["quantity"]
        grand_total += total_cost
        display_total(item)
        more_items = input("Do you want to add another item? (y/n): ").strip().lower()
        if more_items != 'y':
            break
    return items,grand_total,total_quantity

# Function to display the grand total
def display_grand_total(grand_total, note=""):
    print(f"\nGrand Total for all items {note} : {grand_total:.2f}")
    
    

# -------------------------------------------------------------
# -------------------------------------------------------------


# Coding Challenge 27: Applying Discounts

def apply_discounts(grand_total, total_quantity):
    discount_details = []
    total_general_discount = 0.0
    # Rule 1: 10% discount if grand total exceeds ₹10,000
    if grand_total > 10000:
        discount_amount = grand_total * 0.10
        grand_total -= discount_amount
        total_general_discount += discount_amount
        discount_details.append(f"10% discount applied: -₹{discount_amount:.2f}")
    
    # Rule 2: Additional 5% discount if total quantity exceeds 20
    if total_quantity > 20:
        discount_amount = grand_total * 0.05
        grand_total -= discount_amount
        total_general_discount += discount_amount
        discount_details.append(f"5% quantity discount applied: -₹{discount_amount:.2f}")
    
    return grand_total, discount_details, total_general_discount

# Function to display discounts applied
def display_discounts(discount_details, grand_total):
    for detail in discount_details:
        print(detail)
    display_grand_total(grand_total,"after discounts")
    
# -------------------------------------------------------------
# -------------------------------------------------------------

# Coding Challenge 28: Membership Discounts

# Function to check membership status
def check_membership():
    while True:
        membership = input("Are you a member? (y/n): ").strip().lower()
        if membership in ['y', 'n']:
            return membership == 'y'
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

# Function to apply membership discount
def apply_membership_discount(grand_total, is_member):
    discount_amount = 0.0
    if is_member:
        discount_amount = grand_total * 0.02
        grand_total -= discount_amount
        print(f"Membership discount applied: -₹{discount_amount:.2f}")
    return grand_total, discount_amount

# -------------------------------------------------------------
# -------------------------------------------------------------

# Coding Challenge 29: Tax Calculation Based on Purchase Amount 

# Function to calculate tax based on grand total
def calculate_tax(grand_total):
    if grand_total < 5000:
        tax_rate = 0.05
    elif 5000 <= grand_total <= 20000:
        tax_rate = 0.10
    else:
        tax_rate = 0.15
    tax_amount = grand_total * tax_rate
    return tax_amount

# Function to apply tax to grand total
def apply_tax(grand_total):
    tax_amount = calculate_tax(grand_total)
    grand_total += tax_amount
    return grand_total

# Function to display tax amount and updated grand total
def display_tax_and_total(tax_amount, grand_total):
    print(f"Tax Amount: ₹{tax_amount:.2f}")
    display_grand_total(grand_total,"after tax")
    
# -------------------------------------------------------------
# -------------------------------------------------------------

#Coding Challenge 30: Promotional Discounts on Specific Items 

# Function to apply promotional discounts
def apply_promotional_discounts(items,grand_total):
    promotional_codes = {"PROMO10": 0.10}
    total_discount = 0.0
    for item in items:
        if item["item_code"] in promotional_codes:
            discount_amount = item["total_cost"] * promotional_codes[item["item_code"]]
            total_discount += discount_amount
            item["discount"] = discount_amount
            print(f"Promotional discount applied on item {item['item_description']} - {item['item_code']} : -₹{discount_amount:.2f}")
        else:
            item["discount"] = 0.0
    grand_total = grand_total - total_discount
    return grand_total, total_discount

# -------------------------------------------------------------
# -------------------------------------------------------------

# Coding Challenge 31: Payment Mode Rules 

# Function to apply payment mode rules
def apply_payment_mode_rules(grand_total):
    while True:
        payment_mode = input("Select payment mode (Type 'cash' for Cash/ Type 'card' for Credit Card): ").strip().lower()
        if payment_mode == 'cash':
            surcharge = 0.0
            print("No surcharge applied for Cash payment.")
            break
        elif payment_mode == 'card':
            surcharge = grand_total * 0.02
            grand_total += surcharge
            print(f"Surcharge for Credit Card payment applied: ₹{surcharge:.2f}")
            break
        else:
            print("Invalid input. Please enter 'cash' or 'card'.")
    return grand_total, surcharge

# -------------------------------------------------------------
# -------------------------------------------------------------

# Coding Challenge 32: Minimum Purchase Requirements 

# Function to check minimum purchase requirement
def check_minimum_purchase(grand_total):
    if grand_total < 500:
        print("Minimum purchase amount of ₹500 not met. Cannot generate invoice.")
        return False
    return True

# -------------------------------------------------------------
# ------------------------------------------------------------- 

# Coding Challenge 33: Loyalty Points

# Function to calculate loyalty points
def calculate_loyalty_points(grand_total):
    points = int(grand_total // 100)
    return points

# Function to display loyalty points
def display_loyalty_points(points):
    print(f"{'Loyalty Points Earned:':<45} {points}")
    
# Function to display invoice
def display_invoice(items, grand_total, tax_amount, surcharge, promo_discount, general_discount, membership_discount):
    print("\n" + "="*60)
    print(f"{'INVOICE':^60}")
    print("="*60)
    print(f"{'Item':<20} {'Qty':<5} {'Price':<10} {'Total':<10} {'Discount':<10}")
    print("-" * 60)
    
    for item in items:
        discount = item.get("discount", 0.0)
        print(f"{item['item_description']:<20} {item['quantity']:<5} {item['price']:<10.2f} {item['total_cost']:<10.2f} {discount:<10.2f}")
    
    print("-" * 60)
    print(f"{'Total Promotional Discount:':<45} -₹{promo_discount:.2f}")
    print(f"{'Total General Discount:':<45} -₹{general_discount:.2f}")
    print(f"{'Membership Discount:':<45} -₹{membership_discount:.2f}")
    print(f"{'Tax Amount:':<45} ₹{tax_amount:.2f}")
    print(f"{'Surcharge:':<45} ₹{surcharge:.2f}")
    print("-" * 60)
    print(f"{'Final Grand Total:':<45} ₹{grand_total:.2f}")
    
    points = calculate_loyalty_points(grand_total)
    display_loyalty_points(points)
    print("="*60 + "\n")


# Main block to execute the program
if __name__ == "__main__":

    def print_section_header(title):
        print("\n" + "-"*60)
        print(f"{title:^60}")
        print("-" * 60)
    
    # Challenge 25: Basic Item Entry and Total Calculation
    # item = user_input_item()
    # total_cost = compute_total(item["quantity"], item["price"])
    # item.update({"total_cost": total_cost})
    # display_total(item)
    
    print_section_header("Item Entry")
    # Challenge 26: Iterative Item Entry and Grand Total
    items, grand_total,total_quantity = iterative_item_entry()
    display_grand_total(grand_total,"after items entry")

    print_section_header("Promotional Discounts")
    # Coding Challenge 30: Promotional Discounts on Specific Items 
    grand_total, promo_discount = apply_promotional_discounts(items, grand_total)
    display_grand_total(grand_total,"after promotional discounts")
    
    print_section_header("General Discounts")
    # Coding Challenge 27: Applying Discounts
    grand_total, discount_details, general_discount = apply_discounts(grand_total, total_quantity)
    display_discounts(discount_details, grand_total)
    
    print_section_header("Membership Discount")
    # Coding Challenge 28: Membership Discounts

    is_member = check_membership()
    grand_total, membership_discount = apply_membership_discount(grand_total, is_member)
    display_grand_total(grand_total,"after membership discount")
    
    print_section_header("Tax Calculation")
    # Coding Challenge 29: Tax Calculation Based on Purchase Amount 
    tax_amount = calculate_tax(grand_total)
    grand_total = apply_tax(grand_total)
    display_tax_and_total(tax_amount, grand_total)
    
    print_section_header("Payment Mode")
    # Coding Challenge 31: Payment Mode Rules 
    grand_total, surcharge = apply_payment_mode_rules(grand_total)
    display_grand_total(grand_total,"after payment mode rules")
    
    # Coding Challenge 32: Minimum Purchase Requirements 
    if not check_minimum_purchase(grand_total):
        exit()
        
    # Coding Challenge 33: Loyalty Points and invoice display
    display_invoice(items, grand_total, tax_amount, surcharge, promo_discount, general_discount, membership_discount)
    
    
    
