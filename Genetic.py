""" Amirhossein Azimyzadeh Spring 2019 """

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


def first_generation(n_of_population):  # return first generation
    return [Individual(random.uniform(-100, 100), random.uniform(-100, 100)) for p in range(n_of_population)]


def child_creator(parent1, parent2, mutation_prob):
    if mutation_prob == -1:
        mutation_prob = 0.1
    else:
        mutation_prob = mutation_prob
    x_from_parent1 = (random.uniform(-1, 1) < 0)
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


def next_generation(population, fitness_array, mutation_prob):
    next_gen = []
    len_of_pop = len(population)
    for i in range(int(len_of_pop / 2)):
        ind1 = find_max(population, fitness_array)
        ind2 = find_max(population, fitness_array)
        children = child_creator(ind1, ind2, mutation_prob)
        next_gen.insert(0, children[0])
        next_gen.insert(0, children[1])
    return next_gen


def find_max(population, fitness_array):
    max_fit = -math.inf
    max_index = -1
    for i in range(len(fitness_array)):
        if fitness_array[i] > max_fit:
            max_fit = fitness_array[i]
            max_index = i
    fitness_array.pop(max_index)
    return population.pop(max_index)


# -------------------------- print functions ----------------------------
def print_population(population):
    for i in range(len(population)):
        print('(X:' + str(population[i].x) + ',Y:' + str(population[i].y) + ')   \tF =' + str(population[i].f))


def print_prob(prob_array):
    for i in prob_array:
        print(i)


# ------------------------------------------------------------------------
def genetic_al(n_generation, n_population, mutation):
    population = first_generation(n_population)
    fit_array = fitness(population)
    for i in range(n_generation):
        population = next_generation(population, fit_array, mutation)
        fit_array = fitness(population)
    return find_max(population, fit_array).f


number_of_generation = int(input('number of generation :'))
number_of_population = int(input('number of population :'))
mutation_prob = float(input('mutation prob:'))

print(genetic_al(number_of_generation, number_of_population, mutation_prob))
