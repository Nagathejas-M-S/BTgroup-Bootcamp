'''
Coding Challenge 55: Write a program to create a 2D array and display its elements 
row-wise 

Coding Challenge 56: Create a program to compute the sum of all elements in a 2D 
array. 

Coding Challenge 57: Write a program to check if a given element exists in a 2D array 
'''

# Function to input number of rows and columns
def input_rows_and_columns():   
    while True:
        try:
            rows = int(input("Enter the number of rows (positive integer): "))
            cols = int(input("Enter the number of columns (positive integer): "))
            if rows < 1 or cols < 1:
                print("Please enter positive integers greater than 0 for both rows and columns.")
                continue
            return rows, cols
        except ValueError:
            print("Invalid input. Please enter valid positive integers for rows and columns.")

# Function to create 2D array row-wise
def create_2d_array(rows, cols):
    array_2d = []
    print(f"Enter the elements of the 2D array ({rows}x{cols}):")
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    element = int(input(f"Element [{i+1}][{j+1}]: "))
                    row.append(element)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
        array_2d.append(row)
    return array_2d


# Function to display 2D array row-wise
def display_2d_array(array_2d):
    print("The 2D array elements row-wise are:")
    for row in array_2d:
        for element in row:
            print(element, end=" ")
        print()  # New line after each row
        
# Function to check if a given element exists in a 2D array
def check_element_in_2d_array(array_2d):
    while True:
        try:
            target = int(input("Enter the element to search for in the 2D array: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
    for i, row in enumerate(array_2d):
        for j, element in enumerate(row):
            if element == target:
                print(f"Element {target} found at position [{i+1}][{j+1}].")
                return
    print(f"Element {target} not found in the 2D array.")
    
    
        

# Function to compute the sum of all elements in a 2D array
def compute_sum_2d_array(array_2d):
    total_sum = 0
    for row in array_2d:
        total_sum += sum(row)
    print("The sum of all elements in the 2D array is:", total_sum)
    return total_sum

# Main block to execute the program
if __name__ == "__main__":
    
    # Input for number of rows and columns
    rows, cols = input_rows_and_columns()
    
    # Create the 2D array 
    array_2d = create_2d_array(rows, cols)
    
    # Display the 2D array 
    display_2d_array(array_2d)
    
    # Compute the sum of all elements in the 2D array
    total_sum = compute_sum_2d_array(array_2d)
    
    # Check if a given element exists in the 2D array
    check_element_in_2d_array(array_2d)
    
    
    
    
    
    
    