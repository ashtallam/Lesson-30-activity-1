from abc import ABC, abstractmethod

class Absclass(ABC):
    def print(self, x):
        print("Passed value is: ",x)
        @abstractmethod
        def task(self):
            print("We are in Absclass tank")
class test_class(Absclass):
    def task(self):
        print("We are in test_class tank")

test_obj= test_class()
test_obj.task()
test_obj.print(100)

