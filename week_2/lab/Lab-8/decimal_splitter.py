class DecimalSplitter:
    
    """
    Method to get the whole number from a double
    """
    @staticmethod
    def get_whole(number):
        return int(number)

    """
    Method to get the fractional part of a double number
    """
    @staticmethod
    def get_fraction(number):
        return round(number - int(number), 3)


