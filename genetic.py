import random

# Length of chromosome
B = 8  

def fitness(individual):
    return sum(individual)

def select(population, fitness_values):
    return random.choices(population, weights=fitness_values, k=2)

def crossover(p1, p2):
    point = random.randint(1, len(p1) - 1)
    return (
        p1[:point] + p2[point:],
        p2[:point] + p1[point:]
    )

def mutate(individual, rate=0.1):
    return [
        1 - gene if random.random() < rate else gene
        for gene in individual
    ]

# Initial population
population = [[random.randint(0, 1) for _ in range(B)] for _ in range(10)]

# Evolution
for gen in range(50):
    fitness_values = [fitness(ind) for ind in population]
    new_population = []

    for _ in range(len(population) // 2): 
        p1, p2 = select(population, fitness_values)
        c1, c2 = crossover(p1, p2)
        c1, c2 = mutate(c1), mutate(c2)
        new_population.extend([c1, c2])

    population = new_population

# Best individual
best = max(population, key=fitness)
print("Best individual:", best, "Fitness:", fitness(best))
  