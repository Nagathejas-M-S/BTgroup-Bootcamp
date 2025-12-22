from result_finder import ResultFinder

class Program:
    @staticmethod
    def main(args):
        # # Accept the values from command line arguments
        # marks1 = int(args[0])
        # marks2 = int(args[1])
        # marks3 = int(args[2])
        
        def input_marks(subject_number):
            while True:
                try:
                    marks = int(input(f"Enter marks for subject {subject_number} (0-100): "))
                    if 0 <= marks <= 100:
                        return marks
                    else:
                        print("Please enter a valid mark between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter an integer value.")
        
        # Accept the values from user input
        
        print("Please enter the marks for 3 subjects:") 
        marks1 = input_marks(1)
        marks2 = input_marks(2)
        marks3 = input_marks(3)

        # Store the values entered in the object
        finder = ResultFinder()
        finder.marks1 = marks1
        finder.marks2 = marks2
        finder.marks3 = marks3

        # Display all the information with the help of get and other methods
        print("Marks entered------------- ")
        print("Marks 1 : " + str(finder.marks1))
        print("Marks 2 : " + str(finder.marks2))
        print("Marks 3 : " + str(finder.marks3))
        print("Total : " + str(finder.get_total()))
        print("Average : " + str(finder.get_average()))
        print("Result : " + str(finder.get_result()))

        input()


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
