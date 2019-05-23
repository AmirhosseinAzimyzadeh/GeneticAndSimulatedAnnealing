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
        self.f = f(x, y)


def generate_first_node():  # generate first node randomly
    return Node(random.uniform(-10, 10), random.uniform(-10, 10))


def generate_next_node(current_node, change_prob):  # change_prob : Probability of changing x or y or both of them
    select_state_prob = random.uniform(1, 4)
    # 3 state for creating next node
    if 4 > select_state_prob >= 3:
        x = current_node.x * random.uniform(1 - change_prob, 1 + change_prob)
        y = current_node.y
        return Node(x, y)
    elif 3 > select_state_prob >= 2:
        x = current_node.x
        y = current_node.y * random.uniform(1 - change_prob, 1 + change_prob)
        return Node(x, y)
    elif 2 > select_state_prob >= 1:
        x = current_node.x * random.uniform(1 - change_prob, 1 + change_prob)
        y = current_node.y * random.uniform(1 - change_prob, 1 + change_prob)
        return Node(x, y)


def temperature_probability(delta_e, temperature):
    return math.exp((delta_e / temperature))


def simulated_annealing(temperature, change_prob):
    current_node = generate_first_node()
    while temperature > 0:
        next_node = generate_next_node(current_node, change_prob)
        delta_e = math.fabs(next_node.f) - math.fabs(current_node.f)
        if delta_e > 0:
            current_node = next_node
        else:
            if random.uniform(0, 1) <= temperature_probability(delta_e, temperature):
                # print(delta_e)
                current_node = next_node
        temperature = temperature - 1
    return current_node


# if you repeat simulated annealing for n time result will get better
def iterative_sa(t, cp):
    a = []
    for i in range(100):
        a.append(simulated_annealing(t, cp))
    min_ = math.inf
    for i in range(len(a)):
        if a[i].f < min_:
            min_ = a[i].f
    return min_


print(simulated_annealing(1000, 0.1).f)
print(iterative_sa(1000, 0.1))

