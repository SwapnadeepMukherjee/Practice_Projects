class Student:
    school = 'Tulesko'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Instance method -
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # Class Method -
    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print('This is student class.. in abc module')

    # Getters(Accessors):
    # def get_m1(self):
    #     return self.m1
    #
    # Setters(Mutators):
    # def set_m1(self,value):
    #     self.m1 = value


s1 = Student(34, 67, 32)
s2 = Student(89, 32, 93)

print(s1.avg())
print(Student.getschool())
Student.info()