# 3. Create a class ‘Employee’ and add salary and increment properties to it.


class Employee :
    salary = 250
    increment = 40

    @property
    def SalaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary) -1)*100


e = Employee()
e.SalaryAfterIncrement = 300
print(e.increment)