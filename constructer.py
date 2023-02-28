class Demo:
    def __init__(self):
        print('1st constructor')
    def __init__(self,a):
        print('2st constructor')
    def __init__(self,a,b):
        print('3st constructor')
    def fun(self):
        print('normal method')
d=Demo()
d.fun()

