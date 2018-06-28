from Advanced.ChildClass import ITEmployee
from Advanced.Employee_Class import Employee

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print("EMPLOYEE COUNT : ", Employee.empCount)
print("EMPLOYEE : ", Employee.__module__)

emp3 = ITEmployee()
emp3.displayEmployee()

print("EMPLOYEE COUNT : ", Employee.empCount)
