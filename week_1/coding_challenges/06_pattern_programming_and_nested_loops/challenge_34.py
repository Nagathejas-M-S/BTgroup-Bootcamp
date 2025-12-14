# Coding Challenge 34: Printing Star Pattern (N Rows) 
# Coding Challenge 34: Printing Number Pattern (N Rows)

# Function to print the star pattern
def print_star_pattern(n):
    for i in range(n):
        print('*'*n)
    
# Function to print the number pattern
def print_number_pattern(n):
    for i in range(n):
        for j in range(1, n + 1):
            print(j,end='')
        print()
        
        
# Main block to execute the program
if __name__ == "__main__":
    while True:
        try:
            N = int(input("Enter a positive integer N: "))
            if N < 1:
                print("Please enter a positive integer greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")
# Call the function to display the star pattern
    print_star_pattern(N)
# Call the function to display the number pattern
    print_number_pattern(N)
