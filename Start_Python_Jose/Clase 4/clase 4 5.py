
class Students:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

class Workstudents(Students):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property #esto transforma el metodo en una propiedad, simplifica su uso
    def weeksal (self):
        return self.salary * 37.5

rolf = Workstudents('Rolf', 'MIT', 15.5)
rolf.marks.append([45,60,80,90])
print(rolf.marks)
print(rolf.weeksal)
