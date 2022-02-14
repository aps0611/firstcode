#READ ONLY properties by which values cannot be changed by assignment operator =

class Employee:
    def __init__(self, basesalary, yearsofworking):
        self.basesalary = basesalary
        self.yearsofworking = yearsofworking
      
    @property
    def salary(self):
        return (self.basesalary) * (self.yearsofworking)
  #now that we have property function added here and no setter we have made salary read only
  #if anyone tries to change amit.salary = 21212 random it is not possible and it will show Attribute Error.

amit = Employee(20000, 5)

print(amit.basesalary, amit.yearsofworking)

#amit.salary = 10000