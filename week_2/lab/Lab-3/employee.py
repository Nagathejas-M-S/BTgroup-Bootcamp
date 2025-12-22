"""
Class to represent employee information
"""
class Employee:
    def __init__(self):
        self._emp_id = ""
        self._name = ""
        self._gender = ""
        self._address = None
        
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
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, value):
        self._gender = value    
        
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, value):
        self._address = value
        
    