class Calc:

    def add(self, *args):
        result = 0
        for i in args:
            result += i
        print(result)


obj = Calc()
num = [1, 2, 3]
obj.add(num)
