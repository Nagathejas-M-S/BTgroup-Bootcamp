from decimal_splitter import DecimalSplitter

class Program:
    @staticmethod
    def main(args):
        number = 0.0
        # Accept the value through command prompt
        # number = float(args[0])
        
        def input_number():
            while True:
                try:
                    number = float(input(f"Enter a decimal number: "))
                    return number  
                except ValueError:
                    print("Invalid input. Please enter an decimal value.")
        
        # Accept the values from user input
        
        number = input_number()

        # Display the whole and the fractional part from the given number
        print("Number entered is : " + str(number))
        print("Whole part of the given number is : " + str(DecimalSplitter.get_whole(number)))
        print("Fractional part of the given number is : " + str(DecimalSplitter.get_fraction(number)))

        input()


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
