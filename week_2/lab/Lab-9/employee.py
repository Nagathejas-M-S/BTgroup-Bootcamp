class Employee:
    """
    Properties of the class
    """
    def __init__(self):
        self._emp_id = ""
        self._name = ""
        self._basic = 0.0
        self._hra = 0.0
        self._allowance_percentage = 0.0
        self._role = 0
        
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
        
        