from employee_report import EmployeeReport
from role_builder import RoleBuilder
from roles import Roles
from employee import Employee

class Program:
    @staticmethod
    def main(args):
        # Employee array to hold the employees' information
        employees = [None] * 4
    

        # Accept employee information from the user
        print("Enter employee information")

        for i in range(len(employees)):
            emp = Employee()
            
            print("Employee No : " + str(i+1))
            
            print("Id : ")
            emp.emp_id = input()

            print("Name : ")
            emp.name = input()

            print("Basic : ")
            emp.basic = float(input())

            print("HRA : ")
            emp.hra = float(input())

            print("Percentage of Allowance : ")
            emp.allowance_percentage = float(input())

            print("Enter Role Id : ")
            print(str(Roles.DEVELOPER.value) + ". " + RoleBuilder.get_role_description(Roles.DEVELOPER.value))
            print(str(Roles.TEST_ENGINEER.value) + ". " + RoleBuilder.get_role_description(Roles.TEST_ENGINEER.value))
            print(str(Roles.SR_DEVELOPER.value) + ". " + RoleBuilder.get_role_description(Roles.SR_DEVELOPER.value))
            print(str(Roles.DESIGNER.value) + ". " + RoleBuilder.get_role_description(Roles.DESIGNER.value))
            emp.role = int(input())
            employees[i] = emp

            # Note: Original C# code does not assign Employee object to Employees array

        print("Enter the date of the report (dd/mm/yyyy) : ")
        dt_report = input()

        report = EmployeeReport(dt_report)
        report.display_employees(employees)

        input()


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
