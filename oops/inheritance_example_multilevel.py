class Grand_Father:

    def car(self):
        print("Grand Father's car")


class Father(Grand_Father):

    def bike(self):
        print("Dad's bike - Hero Honda Splendor")


# inheritance
class Son(Father):
    pass


obj = Son()
obj.bike()
obj.car()
