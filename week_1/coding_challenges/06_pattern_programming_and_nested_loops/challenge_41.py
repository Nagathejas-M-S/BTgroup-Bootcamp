'''
Coding Challenge 41: Convert Number to Words Using Mathematical Logic  
a. Input: 270176  
b. Output: Two Seven Zero One Seven Six
'''

def number_to_words(num):
    # Dictionary to map digits to words
    digit_to_word = {
        '0': 'Zero',
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine'
    }
    
    digits = []
    
    while num > 0:
        digit = num % 10
        digits.append(digit_to_word[str(digit)])
        num //= 10

    # Reverse the list to get the correct order
    digits.reverse()
    
    # Join the words with spaces and return
    return ' '.join(digits)

# Main block to execute the program
if __name__ == "__main__":
    while True:
        try:
            N = int(input("Enter a positive integer N: "))
            if N < 0:
                print("Please enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid non-negative integer.")

    # Call the function to convert number to words and display the result
    result = number_to_words(N)
    print(result)
    
    