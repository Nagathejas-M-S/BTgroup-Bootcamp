class ResultFinder:
    """
    Properties of the fields of this class
    """
    def __init__(self):
        self._marks1 = 0
        self._marks2 = 0
        self._marks3 = 0
        
    @property
    def marks1(self):
        return self._marks1
    
    @marks1.setter
    def marks1(self, value):
        self._marks1 = value
        
    @property
    def marks2(self):
        return self._marks2
    
    @marks2.setter
    def marks2(self, value):
        self._marks2 = value
        
    @property
    def marks3(self):
        return self._marks3
    
    @marks3.setter
    def marks3(self, value):
        self._marks3 = value

    """
    Method to display marks obtained
    """
    def display_marks(self):
        print("Marks 1 : " + str(self.marks1))
        print("Marks 2 : " + str(self.marks2))
        print("Marks 3 : " + str(self.marks3))

    """
    Method to get the total of the marks in subjects
    """
    def get_total(self):
        return self.marks1 + self.marks2 + self.marks3

    """
    Method to calculate the average of the marks
    """
    def get_average(self):
        total = self.get_total()
        average = total / 3
        return round(average, 2)

    """
    Method to get the result for the marks given
    """
    def get_result(self):
        average = self.get_average()
        if self.marks1 < 35 or self.marks2 < 35 or self.marks3 < 35:
            return "Fail"
        elif average >= 85:
            return "Distinction"
        elif average >= 60:
            return "First Class"    
        elif average >= 50:
            return "Second Class"
        elif average >= 35:
            return "Pass Class"
        else:
            return "Fail"
