from abc import ABC,abstractmethod
class Calculator(ABC):
    @absractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
      pass

class Calci1(Calculator):
    def add(self):
        a=10
        b=20
        print(a+b)

    def sub(self):
        a=10
        b=20
        print(a-b)
        
class Calci2(Calculator):
    def add(self):
        a=20
        b=30
        print(a+b)

    def sub(self):
        a=20
        b=30
        print(a-b)
        
c=Calci1()
c.add()
c.sub()

c=Calci2()
c.add()
c.sub()
