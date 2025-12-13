# Coding Challenge 20: Display the Series 1,2,4,7,11,16,22…N

# Function to display the series
def display_series(n):
    current = 1
    for i in range(1, n + 1):
        print(current, end=', ' if i < n else '')
        current += i
        
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
