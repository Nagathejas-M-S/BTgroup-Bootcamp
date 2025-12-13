# Coding Challenge 9: Program to check if a year given is a leap year or not 

# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a leap year."
    else:
        return f"{year} is not a leap year."
    
# Function to get user input and validate it
def input_year():   
    while True:
        try:
            year = int(input("Enter a year (e.g., 2024): ")) # Typecasting input string to integer
            
            if year < 0:
                print("Year cannot be negative. Please enter a valid year.")
                continue
            
            return year
        except ValueError:
            print("Invalid input. Please enter a valid year.")
            
# Main block to execute the program
if __name__ == "__main__":
    year = input_year()
    print(is_leap_year(year))
    
    
    