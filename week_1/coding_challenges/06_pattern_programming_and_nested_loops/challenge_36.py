# Coding Challenge 36: Printing number Increasing Pattern (N Rows)

# Function to print the number Increasing Pattern
def print_number_increasing_pattern(n):
    for i in range(1, n+1):
        print(f"{i}" * i,end='')
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

# Call the function to display the number increasing pattern
    print_number_increasing_pattern(N)