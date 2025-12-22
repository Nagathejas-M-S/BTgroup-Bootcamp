# Function to display the series
def display_series(n):
    start = 5
    add_a = 1
    add_b = 1
    for i in range(1, n + 1):
        print(start, end=' ')
        start += add_a
        add_a , add_b = add_b, add_a + add_b
     
     
# Main block to execute the program   
if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the number of terms: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            display_series(n)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


    
        


        