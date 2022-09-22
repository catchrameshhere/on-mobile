class Login:

    def __init__(self):
        self.username = ""
        self.__password = ""

    def validate(self):
        print("username = ", self.username)
        print("password = ", self.__password)

    def set_password(self, pwd):
        self.__password = pwd

    # def get_password(self):
    #     return self.__password


ramesh = Login()
ramesh.username = "ramesh@gmail.com"
ramesh.set_password("test1234")
ramesh.validate()

print("********from external source*******")
print(ramesh.username)
print(ramesh._Login__password) # Python allows to access pvt variable or methods using this approach