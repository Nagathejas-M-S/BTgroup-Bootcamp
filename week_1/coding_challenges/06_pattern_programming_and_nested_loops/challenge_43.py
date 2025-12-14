'''
Coding Challenge 43: Whole and Fraction value separation 
Write a program to accept a double value. Separate the whole value from the fractional value and 
store them in two variables. Display the same. 
'''

# Function to separate whole and fractional parts
def separate_whole_fraction(value):
    whole_part = int(value)
    # rounding to avoid floating point precision issues
    fractional_part = round(value - whole_part, 10)  
    
    return whole_part, fractional_part

# Function to take user input
def get_user_input():
    while True:
        try:
            user_input = float(input("Enter a double value: "))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid double value.")
            
# Function to display the results
def display_separated_values(whole, fraction):
    print(f"Whole part: {whole}")
    print(f"Fractional part: {fraction}")
    
# Main block to execute the program
if __name__ == "__main__":
    user_value = get_user_input()
    whole, fraction = separate_whole_fraction(user_value)
    display_separated_values(whole, fraction)
    
    