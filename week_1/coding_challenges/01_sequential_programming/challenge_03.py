# Coding Challenge 3: Program to calculate the discount on the total amount

# Function to calculate discount
def calculate_discount(total_amount, discount_rate):
    discount = (total_amount * discount_rate) / 100
    return discount


# Function to get a non-negative float (for amounts)
def get_non_negative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative value.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


# Function to get a valid discount rate between 0 and 100
def get_discount_rate(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0 or value > 100:
                print("Discount rate must be between 0 and 100.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Main block to execute the program
if __name__ == "__main__":
    # Get total amount from user (>= 0)
    total_amount = get_non_negative_float("Enter the total amount: ")

    # Get discount rate from user (0–100)
    discount_rate = get_discount_rate("Enter the discount rate (in %): ")

    # Calculate discount
    discount = calculate_discount(total_amount, discount_rate)
    final_price = total_amount - discount

    # Display the result
    print(f"The discount on the total amount of {total_amount} at a rate of {discount_rate}% is: {discount}")
    print(f"The final price after discount is: {final_price}")
