# Coding Challenge 18: Display the Series 1,3,5,7,9…N 

# Function to display the series from 1 to N with odd numbers
def display_series(n):
    for i in range(1, n + 1, 2):
        print(i, end=', ' if i < n else '')
        
# Main block to execute the program
if __name__ == "__main__":
    while True:
        try:
            N = int(input("Enter a positive integer N: "))
            if N <= 0:
                print("Please enter a positive integer greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")
# Call the function to display the series
    display_series(N)