# Coding Challenge 8: To find the largest of 3 numbers 

# Function to find the largest of three numbers
def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

# Function to get number
def get_number(prompt):
    while True:
        try:
            num = float(input(prompt)) # Typecasting input string to float
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to get user input and validate it
def input_numbers():    
        num1 = get_number("Enter the first number: ")# Typecasting input string to float
        num2 = get_number("Enter the second number: ") # Typecasting input string to float
        num3 = get_number("Enter the third number: ") # Typecasting input string to float
        return num1, num2, num3
            
# Main block to execute the program
if __name__ == "__main__":
    num1, num2, num3 = input_numbers()
    largest = find_largest(num1, num2, num3)
    print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")