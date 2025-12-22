from salary_calculator import SalaryCalculator
class Employee:
    """
    Properties of the class
    """
    def __init__(self, emp_id="", name="", basic=0.0, hra=0.0, allowance_percentage=0.0, role=0):
        self._emp_id = emp_id
        self._name = name
        self._basic = basic
        self._hra = hra
        self._allowance_percentage = allowance_percentage
        self._role = role
        
    @property
    def emp_id(self):
        return self._emp_id
    
    @emp_id.setter
    def emp_id(self, value):
        self._emp_id = value
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def basic(self):
        return self._basic  
    
    @basic.setter
    def basic(self, value):
        self._basic = value
        
    @property
    def hra(self):
        return self._hra
    
    @hra.setter
    def hra(self, value):
        self._hra = value
        
    @property
    def allowance_percentage(self):
        return self._allowance_percentage
    
    @allowance_percentage.setter
    def allowance_percentage(self, value):
        self._allowance_percentage = value
        
    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, value):
        self._role = value  
        
    def get_allowance(self):
        return SalaryCalculator.get_allowance(self)
    
    def get_salary(self):
        return SalaryCalculator.get_salary(self)
        
        