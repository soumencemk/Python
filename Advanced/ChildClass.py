from Advanced.Employee_Class import Employee


class ITEmployee(Employee):

    def __init__(self):
        print("CHILD CONSTRUCTOR")
        Employee.empCount += 1

    def childMethod(self):
        print('Calling child method')
