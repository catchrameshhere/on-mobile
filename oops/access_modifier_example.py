class Test:
    a = "ramesh" # public variable
    _b = "john" # protected variable
    __c = "michelle" # private variable

    _ = "test"
    __ = "var"

obj = Test()
# print(obj.a)
# print(obj._b)
# print(obj._Test__c)

print(obj.__)
