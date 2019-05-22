import math
import random


class Individual:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f = f(x, y)


def fitness(population):
    # Cross-in-Tray function always return negative value
    # prob. = x.sum * 100
    sum_of_values = 0
    for p in population:
        sum_of_values += p.f
    return [(p.f / sum_of_values) * 100 for p in population]


def f(x, y):
    x = float(x)
    y = float(y)
    a = math.sqrt(x * x + y * y)
    expo = math.exp(math.fabs(100 - (a / math.pi)))
    inside = math.fabs(math.sin(x) * math.sin(y) * expo) + 1
    result = (-0.0001) * math.pow(inside, 0.1)
    return result


def first_generation(n_of_population):  # return first generation
    return [Individual(random.uniform(-10, 10), random.uniform(-10, 10)) for p in range(n_of_population)]


def child_creator(parent1, parent2, mutation_prob):
    mutation_prob = 0.1
    x_from_parent1 = (random.uniform(-1, 1) < 0)
    child1_x = 0
    child1_y = 0
    child2_x = 0
    child2_x = 0

    if x_from_parent1:
        child1_x = parent1.x
        child1_y = parent2.y
        child2_x = parent1.y
        child2_y = parent2.x
    else:
        child1_x = parent2.x
        child1_y = parent1.y
        child2_x = parent1.x
        child2_y = parent2.y

    prob = random.uniform(1 - mutation_prob, 1 + mutation_prob)
    child1 = Individual(child1_x * prob, child1_y) if (random.uniform(-1, 1) < 0) else Individual(child1_x,
                                                                                                  child1_y * prob)
    prob = random.uniform(1 - mutation_prob, 1 + mutation_prob)
    child2 = Individual(child2_x * prob, child2_y) if (random.uniform(-1, 1) < 0) else Individual(child2_x,
                                                                                                  child2_y * prob)

    return [child1, child2]


# -------------------------- print functions ----------------------------
def print_population(population):
    for i in range(len(population)):
        print('(X:' + str(population[i].x) + ',Y:' + str(population[i].y) + ')   \tF =' + str(population[i].f))


def print_prob(prob_array):
    for i in prob_array:
        print(i)


# ------------------------------------------------------------------------

print(f(-5, -6))
number_of_generation = int(input('number of generation :'))
number_of_population = int(input('number of population :'))
print_population(child_creator(Individual(-6, 5), Individual(-10, 1), 0.1))
print('___________')
print_prob(fitness(first_generation(number_of_population)))
