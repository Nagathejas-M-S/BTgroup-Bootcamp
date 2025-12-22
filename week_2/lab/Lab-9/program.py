from employee_report import EmployeeReport
from role_builder import RoleBuilder
from roles import Roles
from employee import Employee

class Program:
    @staticmethod
    def main(args):
        # Employee array to hold the employees' information
        employees = [None] * 4
        emp = None
        
        report_date = ""

        # Accept employee information from the user
        print("Enter employee information")

        for i in range(len(employees)):
            print("Employee No : " + str(i+1))
            emp = Employee()
            
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
            print(str(Roles.DEVELOPER) + ". " + RoleBuilder.get_role_description(Roles.DEVELOPER))
            print(str(Roles.TEST_ENGINEER) + ". " + RoleBuilder.get_role_description(Roles.TEST_ENGINEER))
            print(str(Roles.SR_DEVELOPER) + ". " + RoleBuilder.get_role_description(Roles.SR_DEVELOPER))
            print(str(Roles.DESIGNER) + ". " + RoleBuilder.get_role_description(Roles.DESIGNER))
            emp.role = int(input())
            
            employees[i] = emp

            # Note: Original C# code does not assign Employee object to Employees array

        print("Enter the date of the report (dd/mm/yyyy) : ")
        report_date = input()

        report = EmployeeReport()
        report.report_date = report_date
        report.display_employees(employees)

        input()


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
