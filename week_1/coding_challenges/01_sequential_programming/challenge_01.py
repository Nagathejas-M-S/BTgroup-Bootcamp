# Coding Challenge 1: Program to find the sum and average of two variables 


# Function to calculate sum and average of two numbers
def calculate_sum_and_avg(num1,num2):
    total = num1 + num2
    avg = total / 2
    return total, avg # Return both sum and average as a tuple


# Function to get valid float input from the user
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


# Main block to execute the program
if __name__ == "__main__":
    
    # Taking input from the user
    # Typecasting input to float to handle decimal numbers
    num1 = get_float_input("Enter first number: ")
    num2 = get_float_input("Enter the second number: ")
    
    # Calling the function to calculate sum and average
    total, avg = calculate_sum_and_avg(num1,num2)
    
    # Displaying the results
    print(f"Sum: {total}")
    print(f"Average: {avg}")
