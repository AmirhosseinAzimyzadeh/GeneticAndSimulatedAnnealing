"""" Amirhossein Azimyzadeh Spring 2019 """

import math
import random


# ----------------------------------CROSS IN TRAY FUNCTION-----------------------
def f(x, y):
    x = float(x)
    y = float(y)
    a = math.sqrt(x * x + y * y)
    expo = math.exp(math.fabs(100 - (a / math.pi)))
    inside = math.fabs(math.sin(x) * math.sin(y) * expo) + 1
    result = (-0.0001) * math.pow(inside, 0.1)
    return result


# -------------------------------------------------------------------------------
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def generate_first_node():  # generate first node randomly
    return Node(random.uniform(-100, 100), random.uniform(-100, 100))


def generate_next_node(current_node):
    select_state_prob = random.uniform(0, 4)
