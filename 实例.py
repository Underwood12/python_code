class C():
    pass


def print_attribute(obj):
    for attr in obj.__dict__:
        print(attr, getattr(obj, attr))


class Messager(object):
    def __init__(self, **kwargs):
        self.__dict__ = kwargs


def K():
    N = Messager(a=21, b=2)
    return N

c = C()
print(c.__dict__)
c.age = 10
print(c.__dict__, c.age)
print_attribute(c)
M = Messager(**{"f": 12, "a": 324})
print(M.__dict__)
print(M.a)
print(M.f)
n = Messager(f=21, a=321)
print(n.f)
print(n.__dict__)
print(K().a)
# print(K.a) # AttributeError: 'function' object has no attribute 'a'
