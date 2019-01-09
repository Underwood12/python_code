class Person(object):
    counter = 0

    def __init__(self, age):
        self.age = age
        Person.counter += 1

    def __del__(self):
        Person.counter -= 1


print(Person.counter)
p1 = Person(20)
p2 = Person(21)
p3 = Person(22)
print(Person.counter, p1.counter, p2.counter, p3.counter)
del p1
print(Person.counter, p2.counter, p3.counter)
# print(p1.counter) # NameError: name 'p1' is not defined
p2.counter = 10
print(Person.counter, p2.counter, p3.counter)
Person.counter = 10
print(Person.counter, p2.counter, p3.counter)
print(Person.__bases__)
print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)