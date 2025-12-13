# Coding Challenge 22: Display the Series 1,4,7,12,23…N

# Function to display the series
def display_series(n):
    value = 1
    add = 3
    
    for i in range(1, n + 1):
        print(value, end=", " if i < n else "")
        value += add
        add += i * (i - 1)
        
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
