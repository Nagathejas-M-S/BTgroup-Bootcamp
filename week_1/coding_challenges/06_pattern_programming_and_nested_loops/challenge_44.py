'''
Coding Challenge 44: Reverse of a number 
Write a program to find the reverse of a number. Store the reverse value in a different variable. 
Display the reverse. 
'''

# Function to reverse a number
def reverse_number(num):    
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

# Function to take user input
def get_user_input():   
    while True:
        try:
            user_input = int(input("Enter a positive integer: "))
            if user_input < 0:
                print("Please enter a positive integer.")
                continue
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")
            
# Main block to execute the program
if __name__ == "__main__":
    user_value = get_user_input()
    reversed_value = reverse_number(user_value)
    print(f"Reversed number: {reversed_value}")
    
    