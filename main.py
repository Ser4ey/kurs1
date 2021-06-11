class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('From get_name()')
        return self._name

    def set_name(self, value):
        print('From set_name()')
        self._name = value

    name = property(fget=get_name, fset=set_name)

p1 = Person('Oleg')

print(p1.__dict__)
print(p1.name)
# p1.name = '233'
p1._name = '1234jjjjjj'

print(p1.__dict__)