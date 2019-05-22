import math


class Individual:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f = f(x, y)
        self.fitness = 0

    def set_fitness(self, fit):
        self.fitness = fit


def fitness(population):
    return


def f(x, y):
    x = float(x)
    y = float(y)
    a = math.sqrt(x * x + y * y)
    expo = math.exp(math.fabs(100 - (a / math.pi)))
    inside = math.fabs(math.sin(x) * math.sin(y) * expo) + 1
    result = (-0.0001) * math.pow(inside, 0.1)
    return result


print(f(-5, -6))
