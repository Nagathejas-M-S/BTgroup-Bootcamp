# Coding Challenge 24: Display the Series 1,1,2,3,5,8,13,21…N

# Function to display the series 

def display_series(n):
    a,b = 0,1
    for i in range(1, n + 1):
        print(b, end=", " if i < n else "")
        a, b = b, a + b
        
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
