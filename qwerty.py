class Parent:
    def __init__(self):
        print('parent class Constructer')
class Child(parent):
    def __init__(self):
        super().__init__()
        print('child class constructer')
c=Child()
