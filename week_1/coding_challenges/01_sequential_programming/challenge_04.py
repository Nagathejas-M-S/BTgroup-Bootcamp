# Coding Challenge 4: Program to swap two numbers

# Function to swap two numbers
def swap_numbers(a, b):
    return b, a

# Function to get valid numeric input from the user
def get_valid_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Main block to execute the program
if __name__ == "__main__":
    # Input: Two numbers from the user
    num1 = get_valid_input("Enter the first number: ")
    num2 = get_valid_input("Enter the second number: ")

    # Swapping the numbers using the swap_numbers function
    num1, num2 = swap_numbers(num1, num2)
    
    # Swapping directly without a function
    # num1, num2 = num2, num1

    # Output: Displaying the swapped numbers
    print("After swapping:")
    print("First number:", num1)
    print("Second number:", num2)