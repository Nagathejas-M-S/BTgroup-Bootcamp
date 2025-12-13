# Coding Challenge 7: Program to accept name and salary. Check if their salary is >3L 
# and display if they must pay tax 


def check_tax(name, salary):
    if salary > 300000:
        return f"{name} has to pay tax."
    else:
        return f"{name} does not have to pay tax."
    
def input_name_salary():
    name = input("Enter your name: ")
    while True:
        try:
            salary = float(input("Enter your salary (Example format -> 300000): ")) # Typecasting input string to float
            
            if salary < 0:
                print("Salary cannot be negative. Please enter a valid salary amount.")
                continue
            
            return name, salary
        except ValueError:
            print("Invalid input. Please enter a valid salary amount.")
   
# Main block to execute the program  
if __name__ == "__main__":
    name, salary = input_name_salary()
    result = check_tax(name, salary)
    print(result)