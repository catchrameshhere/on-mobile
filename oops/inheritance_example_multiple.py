class Mother:

    def car(self):
        print("Mom's car - swift")

    def bike(self):
        print("Mother's bike - Activa")


class Father:

    def bike(self):
        print("Dad's bike - Hero Honda Splendor")


# inheritance
class Son(Father, Mother):
    pass


obj = Son()
obj.bike()
obj.car()
