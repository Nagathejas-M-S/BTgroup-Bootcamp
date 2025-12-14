# Coding Challenge 45: Level 0: Write a program to accept n and 
# store the elements into the array of size n.

# Coding Challenge 46: Level 1: Find the Sum of all elements in the array 

# Coding Challenge 47: Level 2: Find the Minimum value of all elements in the array

# Coding Challenge 48: Level 3: Find the Maximum value of all elements in the array

# Coding Challenge 49: Level 4: Search the given element from the array 

# Coding Challenge 50: Level 5: Display the number of odd and even numbers from the array


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
def sum_of_array_elements(elements):
    total_sum = sum(elements)
    print("The sum of all elements in the array is:", total_sum)    

# Function to calculate and display the sum of all elements in the array
def min_of_array_elements(elements):
    minimum_value = min(elements)
    print("The minimum value of all elements in the array is:", minimum_value)
   
    
# Function to calculate and display the sum of all elements in the array
def max_of_array_elements(elements):
    maximum_value = max(elements)
    print("The maximum value of all elements in the array is:", maximum_value)
    

# Function to search for a given element in the array
def search_in_array_elements(elements):
    while True:
        try:
            target = int(input("Enter the element to search in the array: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
    if target in elements:  
        print(f"The element {target} is found in the array at index {elements.index(target)}.")
    else:
        print(f"The element {target} is not found in the array.")
  

# Function to search for a given element in the array
def display_odd_even_count(elements):
    odd_count = 0
    even_count = 0
    for element in elements:
        if element % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
    print(f"Number of odd elements in the array: {odd_count}")
    print(f"Number of even elements in the array: {even_count}")

   
# Main block to execute the program
if __name__ == "__main__":
    # Input number of elements
    N = input_number_of_elements()
    
    # Call the function to store elements in the array
    array_elements = store_elements_in_array(N)
    
    # Display the stored elements
    display_array_elements(array_elements)
    
    print()
    
    # Display the sum of all elements in the array
    sum_of_array_elements(array_elements)
    
    print()
    
    # Display the minimum value of all elements in the array
    min_of_array_elements(array_elements)
    
    print()
    
    # Display the maximum value of all elements in the array
    max_of_array_elements(array_elements)
    
    print()
    
    # Search for a given element in the array
    search_in_array_elements(array_elements)
    
    print()
    
    # Display the count of odd and even numbers in the array
    display_odd_even_count(array_elements)
    
    
 