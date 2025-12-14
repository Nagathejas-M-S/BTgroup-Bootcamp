# Coding Challenge 39: Printing Pattern of Perfect Squares with Alternating Signs in N Rows 

# Function to print the perfect squares with alternating signs pattern
def print_perfect_squares_alternating_signs(n):
    num = 1
    sign = 1
    for i in range(1, n+1):
        for j in range(1, i + 1):
            print(sign*num*num,end=' ')
            num += 1
            sign = -sign
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
    print_perfect_squares_alternating_signs(N)