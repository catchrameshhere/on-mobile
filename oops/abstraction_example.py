from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass


class Seltos(Car):

    def mileage(self):
        print("Mileage = 13KMPL")
        pass


obj = Seltos()
obj.mileage()
