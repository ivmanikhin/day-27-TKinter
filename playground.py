def add(*args):
    summ = 0
    for i in args:
        summ += i
    return summ


print(add(1, 1, 2, 2))


def calc(**kwargs):
    print(kwargs)


calc(add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')


my_car = Car(make='Nissan', model='GTR')
print(my_car.model)