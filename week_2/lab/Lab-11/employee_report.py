from employee import Employee

class EmployeeReport:
    """
    Property of the class
    """
    def __init__(self,dt_report=""):
        self.report_date = dt_report

    """
    Method to print a line in a report
    """
    def print_line(self):
        print("---------------------------------------------------------------------------")

    """
    Method to display header information of the report
    """
    def display_header(self):
        self.print_line()
        print("EMPLOYEE REPORT\t\t\t\t")
        print("Date : " + self.report_date)
        self.print_line()

    """
    Method to display footer information in the report
    """
    def display_footer(self, count):
        self.print_line()
        print("Total Employees : " + str(count))
        self.print_line()

    """
    Method to display employees information
    """
    def display_employees(self, employees):
        self.display_header()

        print("EMP_ID\tNAME\tROLE\t\tBASIC\tHRA\tALLOW\tSALARY")
        self.print_line()
        
        for employee in employees:
            allowance = employee.get_allowance()
            salary = employee.get_salary()
            role_name = employee.get_role_description()
            print(f"{employee.emp_id}\t{employee.name}\t{role_name}\t{employee.basic}\t{employee.hra}\t{allowance}\t{salary}")

        self.display_footer(len(employees))
