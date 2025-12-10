# Coding Challenge 2: Program to calculate simple interest

# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Main block to execute the program
if __name__ == "__main__":
    
    # Taking input from the user
    principal = get_float_input("Enter the principal amount: ")
    rate = get_float_input("Enter the rate of interest (in %): ")
    time = get_float_input("Enter the time period (in years): ")
    
    # Calling the function to calculate simple interest
    interest = calculate_simple_interest(principal, rate, time)
    
    # Displaying the result
    print(f"Simple Interest: {interest}")
    
