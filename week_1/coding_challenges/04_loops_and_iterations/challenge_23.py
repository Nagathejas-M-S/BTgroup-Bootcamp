# Coding Challenge 23: Display the Series 1,5,9,13,21,25,29,37,41…N

# Function to display the series
def display_series(n):
    value = 1
    
    for i in range(1, n + 1):
        print(value, end=", " if i < n else "")
        if value % 16 == 13:
            value += 8
        else:
            value += 4
        
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
