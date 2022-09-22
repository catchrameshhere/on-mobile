class Student:

    def __init__(self, name):
        self.student_name = name

    def m1(self):
        print("Student name = ", self.student_name)


s1 = Student("Michelle")
s1.m1()

print(id(s1))
