class Student:
    company_name = "OnMobile"

    def m1(self, age):
        print("age = ", age)

    def get_company_name(self):
        return self.company_name


obj = Student()
# obj.m1(25)
# print(obj.get_company_name())
obj.company_name = "Edureka"
print(obj.company_name)

obj1 = Student()
print(obj1.company_name)
