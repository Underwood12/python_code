class wolf(object):
    def bark(self):
        print('hoooooowell')

class dog(object):
    def bark(self):
        print('woof')

def barkforme(dogtype):
    dogtype.bark()


my_dog = dog()
my_wolf = wolf()
print(barkforme(my_dog))
print(barkforme(my_wolf))