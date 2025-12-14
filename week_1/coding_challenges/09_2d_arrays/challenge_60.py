'''
Coding Challenge 60: Write a program to multiply two matrices
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

#Function to check if multiplication is possible
def can_multiply(cols_a, rows_b):
    return cols_a == rows_b

# Function to multiply two matrices
def multiply_matrices(matrix_a, matrix_b, rows_a, cols_a, cols_b):
    if not can_multiply(cols_a, len(matrix_b)):
        print("Matrix multiplication not possible with the given dimensions.")
        return None
    result = []
    for i in range(rows_a):
        result_row = []
        for j in range(cols_b):
            sum_product = 0
            for k in range(cols_a):
                sum_product += matrix_a[i][k] * matrix_b[k][j]
            result_row.append(sum_product)
        result.append(result_row)
    return result
    
    

# Main block to execute the program
if __name__ == "__main__":
    
    print("Enter details for the first matrix:")
    # Input for number of rows and columns for first matrix
    rows1, cols1 = input_rows_and_columns()
    
    # Create the first matrix
    matrix1 = create_matrix(rows1, cols1)
    
    # Display the first matrix
    display_matrix(matrix1,"The first matrix elements row-wise are:")
    
    print()
    print("Enter details for the second matrix:")
    
    # Input for number of rows and columns for second matrix
    rows2, cols2 = input_rows_and_columns()
    
    # Create the second matrix
    matrix2 = create_matrix(rows2, cols2)
    
    # Display the second matrix
    display_matrix(matrix2,"The second matrix elements row-wise are:")
    
    # Multiply the two matrices
    result_matrix = multiply_matrices(matrix1, matrix2, rows1, cols1, cols2)
    
    if result_matrix:
        # Display the result matrix
        display_matrix(result_matrix,"The resulting matrix after multiplication is:")
        

    
    
    
    
    
    
    
    
    
    
    
    
    