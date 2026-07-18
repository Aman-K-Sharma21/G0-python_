#  Create a class “Programmer” for storing information of few programmers 
# working at Microsoft


class programmer() :
    company = "Microsoft"

    def __init__(self, name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("Aman",24000000,234687)
r = programmer("rohan",23000000,234677)
print(p.name,p.salary,p.pin,p.company)
print(r.name,r.salary,r.pin,r.company)