class Employee:
    empCount = 0  # Class Attribute
    salarySum = 0

    def __init__(self, name, family, salary, dept):
        self.name = name
        self.family = family
        self.salary = salary
        self.dept = dept
        Employee.empCount += 1
        Employee.salarySum += salary

    def averageSal(self):
        return Employee.salarySum / Employee.empCount  # Return avg value of Salary

    def dispDetails(self):
        print('Name : {}'.format(self.name))
        print('Family : {}'.format(self.family))
        print('Salary : {}'.format(self.salary))
        print('Department : {}'.format(self.dept))
        print('Average Salary : {}'.format(Employee.averageSal(Employee)))

class FullTimeEmployee(Employee):
    def __init__(self,name,family,salary,department):
        Employee.__init__(self,name,family,salary,department)

    def updateSalary(self, salary):
        Employee.salarySum -= self.salary
        self.salary = salary
        Employee.salarySum += salary
        

a = Employee('DHairya','7',250000, 'CS')
B = FullTimeEmployee('Ash','7',150000, 'CS')
a.dispDetails()
print()
B.dispDetails()
print()
B.updateSalary(260000)
print()
B.dispDetails()