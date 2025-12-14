# Coding Challenge 48: Level 3: Find the Maximum value of all elements in the array

# Function to take number of elements input
def input_number_of_elements():
    while True:
        try:
            n = int(input("Enter the size of the array (positive integer N): "))
            if n < 1:
                print("Please enter a positive integer greater than 0.")
                continue
            return n
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

# Function to accept n and store elements into an array
def store_elements_in_array(n):
    elements = []
    for i in range(n):
        while True:
            try:
                element = int(input(f"Enter element {i + 1}: "))
                elements.append(element)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    return elements

# Function to display the elements of the array
def display_array_elements(elements):
    print(len(array_elements), "elements have been stored in the array.")
    print("The elements in the array are:", array_elements)
    
# Function to calculate and display the sum of all elements in the array
def max_of_array_elements(elements):
    maximum_value = max(elements)
    print("The maximum value of all elements in the array is:", maximum_value)
    
# Main block to execute the program
if __name__ == "__main__":
    # Input number of elements
    N = input_number_of_elements()
    
    # Call the function to store elements in the array
    array_elements = store_elements_in_array(N)
    
    # Display the stored elements
    display_array_elements(array_elements)
    
    print() 
    
    # Calculate and display the sum of all elements in the array
    max_of_array_elements(array_elements)
    
 