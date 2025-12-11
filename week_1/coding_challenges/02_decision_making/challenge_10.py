# Coding Challenge 10: Student Report Card Problem 
'''
Write a program to accept a student’s name and scores in three subjects. Display the total, average, 
and class secured based on the following criteria: 
• 1st Class: Average score of 60 and above. 
• 2nd Class: Average score of 50 and above. 
• Pass Class: Average score of 35 and above. 
• Fail: Average score less than 35.
'''

# Function to calculate total, average and class
def calculate_report_card(score1, score2, score3):
    total = score1 + score2 + score3
    average = total / 3
    
    if average >= 60:
        student_class = "1st Class"
    elif average >= 50:
        student_class = "2nd Class"
    elif average >= 35:
        student_class = "Pass Class"
    else:
        student_class = "Fail"
    
    return total, average, student_class

# Function to get user input and validate it
def input_student_details():
    name = input("Enter the student's name: ")
    
    def get_score(prompt):
        while True:
            try:
                score = float(input(prompt))  # Typecasting input string to float
                
                if score < 0 or score > 100:
                    print("Score must be between 0 and 100. Please enter a valid score.")
                    continue
                
                return score
            except ValueError:
                print("Invalid input. Please enter a valid score.")
    
    score1 = get_score("Enter score for subject 1: ")
    score2 = get_score("Enter score for subject 2: ")
    score3 = get_score("Enter score for subject 3: ")
    
    return name, score1, score2, score3

# Function to display report card
def display_report_card(name, total, average, student_class):
    print(f"\nReport Card for {name}:")
    print(f"Total Score: {total}")
    print(f"Average Score: {average:.2f}")
    print(f"Class Secured: {student_class}")

# Main function to execute the program
if __name__ == "__main__":
    name, score1, score2, score3 = input_student_details()
    total, average, student_class = calculate_report_card(score1, score2, score3)
    display_report_card(name, total, average, student_class)
