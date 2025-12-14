'''
Coding Challenge 58: Write a program to store elements into a M * N matrix of 
integer. Display the matrix and its transpose. 

Coding Challenge 59: Write a program to store elements into a M * N matrix of 
integer. Display the matrix and its transpose. 

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

# Function to create matrix
def create_matrix(rows, cols):
    matrix = []
    print(f"Enter the elements of the matrix ({rows}x{cols}):")
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
        matrix.append(row)
    return matrix

# Function to display matrix row-wise
def display_matrix(matrix,message):
    print(message)
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()  # New line after each row    
        
# Function to compute the transpose of a matrix
def transpose_matrix(matrix,rows,cols):
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed

# Main block to execute the program
if __name__ == "__main__":
    
    # Input for number of rows and columns
    rows, cols = input_rows_and_columns()
    
    # Create the matrix
    matrix = create_matrix(rows, cols)
    
    # Display the matrix
    display_matrix(matrix,"The matrix elements row-wise are:")
    
    # Compute and display the transpose of the matrix
    transposed_matrix = transpose_matrix(matrix,rows,cols)
    
    # Display the transposed matrix
    display_matrix(transposed_matrix,"The transposed matrix elements row-wise are:")
    
    
    
    
    
    
    
    
    
    
    