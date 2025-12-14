# Coding Challenge 40: Printing Pattern of Factorials in N Rows

# Function to print the factorials in N rows
def print_factorials_pattern(n):
    num = 1
    current = 1
    for i in range(1, n+1):
        for j in range(1, i + 1):
            current *=  num
            print(current,end=' ')
            num += 1
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

# Call the function to display the perfect squares with alternating signs pattern
    print_factorials_pattern(N)