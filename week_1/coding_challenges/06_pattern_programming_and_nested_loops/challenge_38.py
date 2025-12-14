# Coding Challenge 38: Fibonacci Series Pattern (N Rows)

# Function to print the fibonacci series
def print_fibonacci_series(n):
    a, b = 0, 1 
    for i in range(1, n+1):
        for j in range(1, i + 1):
            print(b,end=' ')
            a, b = b, a + b
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

# Call the function to display the fibonacci series
    print_fibonacci_series(N)
