from employee import Employee
from address import Address

class Program:
    @staticmethod
    def main(args):
        emp = Employee()
        Program.store_data(emp)
        Program.show_data(emp)

    @staticmethod
    def store_data(emp):
        emp.emp_id = "E1001"
        emp.name = "John Doe"
        emp.gender = "Male"
        emp.address = Address()
        emp.address.addr_line1 = "123 Main St"
        emp.address.addr_line2 = "Apt 4B"
        emp.address.city = "Metropolis"
        emp.address.pincode = "123456"

    @staticmethod
    def show_data(emp):
        # ----------------Display the employee information
        # print("Employee Id : ")
        # print("Employee Name : ")
        # print("Employee Gender : ")

        # print("Employee Address : --------------")
        # print("Address 1 : ")
        # print("Address 2 : ")
        # print("City : ")
        # print("PinCode : ")
        # print("----------------------------------")
        
        print()
        print(f"Employee Id : {emp.emp_id}")
        print(f"Employee Name : {emp.name}")
        print(f"Employee Gender : {emp.gender}")
        print("Employee Address : --------------")
        print(f"Address 1 : {emp.address.addr_line1}")
        print(f"Address 2 : {emp.address.addr_line2}")
        print(f"City : {emp.address.city}")     
        print(f"PinCode : {emp.address.pincode}")
        print("----------------------------------")


if __name__ == "__main__":
    Program.main([])
