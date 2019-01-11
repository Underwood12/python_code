class Person(object):

    def __init__(self):
        self.A = 'name'
        self.__B = 'age'
        self.__C__ = 'id'

    def Print(self):
        print(self.A)
        print(self.__B)
        print(self.__C__)


p = Person()
print(p.A)
print(p.__C__)
print(p.__B)