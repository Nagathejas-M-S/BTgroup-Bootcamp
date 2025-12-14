# Coding Challenge 51: Level 0: Write a program to accept n and store the elements into 
# the array of size n. 

# Coding Challenge 52: Level 1: Reverse the given array. 

# Coding Challenge 53: Level 2: Sort the array in ascending or descending order based 
# on input of user 

# Coding Challenge 54: Level 3: Implement Binary Search on the array.

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
    
# Function to reverse the array 
def reverse_array(elements):
    reversed_elements = elements[::-1]
    print("The reversed array is:", reversed_elements)
    return reversed_elements

# Function to sort the array based on user input
def sort_array(elements):
    while True:
        order = input("Enter 'A' to sort in ascending order or 'D' for descending order: ").strip().upper()
        if order == 'A':
            sorted_elements = sorted(elements)
            print("The array sorted in ascending order is:", sorted_elements)
            return sorted_elements
        elif order == 'D':
            sorted_elements = sorted(elements)
            reverse_sorted_elements = sorted_elements[::-1]
            print("The array sorted in descending order is:", reverse_sorted_elements)
            return sorted_elements
        else:
            print("Invalid input. Please enter 'A' or 'D'.") 
    
# Function to perform binary search on the array
def binary_search(elements):
    while True:
        try:
            target = int(input("Enter the element to search for in the array: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    left = 0
    right = len(elements) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if elements[mid] == target:
            print(f"Element {target} found at index {mid}.")
            return
        elif elements[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    print(f"Element {target} not found in the array.")
    
# Main block to execute the program
if __name__ == "__main__":
    # Input number of elements
    N = input_number_of_elements()
    
    # Call the function to store elements in the array
    array_elements = store_elements_in_array(N)
    
    # Display the stored elements
    display_array_elements(array_elements)
    
    # Reverse the array
    reversed_array = reverse_array(array_elements)
    
    # Sort the array based on user input
    sorted_array = sort_array(array_elements)
    
    # Perform binary search on the sorted array
    binary_search(sorted_array)
    
    
    
    
    
 