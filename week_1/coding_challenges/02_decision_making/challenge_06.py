# Coding Challenge 6: Program to check if a number is even or odd

# Function to check if a number is even or odd
def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# Function to get user input and validate it
def input_number():
    while True:
        try:
            num = int(input("Enter an integer number: ")) # Typecasting input string to integer
            return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
# Main function to execute the program  
if __name__ == "__main__":
    num = input_number()
    result = is_even_or_odd(num)
    print(f"The number {num} is {result}.")
    
    