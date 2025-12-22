from swap_data import SwapData

class Program:
    @staticmethod
    def main(args):
        # Accept values from the user
        while True:
            try:
                print("Please enter Number 1 (integer):")
                number1 = int(input())
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        while True:
            try:
                print("Please enter Number 2 (integer):")
                number2 = int(input())
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        # Storing the numbers accepted in SwapData object
        obj = SwapData()
        obj.number1 = number1
        obj.number2 = number2

        # Display numbers before swapping
        obj.display_values("Numbers before Swapping :")
        
        # Swapping the numbers in the object
        obj.swap_values()

        # Display numbers after swapping
        obj.display_values("Numbers after Swapping :")

        input()


if __name__ == "__main__":
    Program.main([])
