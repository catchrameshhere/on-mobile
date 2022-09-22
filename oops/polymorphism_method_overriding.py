class Animal:

    def sound(self):
        print("All animals make sound")


class Dog(Animal):

    # method overriding ==> changing the behavior of the method
    def sound(self):
        print("Dog's bark")


d = Dog()
d.sound()
