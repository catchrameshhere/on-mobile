# class defn
# this is an function
def test():
    print('this is from test method')


class Student:
    # this is a method
    def m1(self):
        print('hello there')

    def m2(self):
        print('from m2 - hello there')


# creating an object of the class
# ramesh = Student()
# ramesh.m1()
#
# test()

if __name__ == '__main__':
    s1 = Student()
    s1.m1()
