# Coding Challenge 19: Display the Series 4,16,36,64…N

# Function to display the series of squares of even numbers from 2 to N
def display_series(n):
    for i in range(2, n + 1, 2):
        print(i*i, end=', ' if i < n else '')
        
# Main block to execute the program
if __name__ == "__main__":
    while True:
        try:
            N = int(input("Enter a positive integer N: "))
            if N < 2:
                print("Please enter a positive integer greater than 1.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")
# Call the function to display the series
    display_series(N*2)