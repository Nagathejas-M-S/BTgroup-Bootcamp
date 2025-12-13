# Coding Challenge 21: Display the Series 1,4,9,25,36,49,81…N

# Function to display the series of squares of natural numbers from 1 to N
def display_series(n):
    for i in range(1, n + 1):
        print(i*i, end=', ' if i < n else '')
        
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
# Call the function to display the series
    display_series(N)
