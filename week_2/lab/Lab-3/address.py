class Address:
    def __init__(self):
        self._addr_line1 = ""
        self._addr_line2 = ""
        self._city = ""
        self._pincode = ""
        
    @property
    def addr_line1(self):
        return self._addr_line1

    @addr_line1.setter
    def addr_line1(self, value):
        self._addr_line1 = value

    @property
    def addr_line2(self):
        return self._addr_line2

    @addr_line2.setter
    def addr_line2(self, value):
        self._addr_line2 = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def pincode(self):
        return self._pincode

    @pincode.setter
    def pincode(self, value):
        self._pincode = value