import pandas as pd
import random as rand
import numpy as np

class GeneticAlgorithm:
    def __init__(self, population, generations, cities, distance_map, crossover_rate, mutation_rate):
        self.population = population
        self.generations = generations
        self.cities = cities
        self.distance_map = distance_map
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

    def initialise(self):
        populations = [self.cities.copy()]
        for i in range(self.population):
            current = self.cities.copy()
            rand.shuffle(current)
            populations.append(current)
        return np.array(populations)

    def calculate_distances(self, individual):
        total_distance = 0.0
        for i in range(len(individual) - 1):
            total_distance += self.distance_map[self.cities.index(i), self.cities.index(i + 1)]
        return total_distance

    def fitness(self, population):
        population_fitness = []
        for individual in population:
            current_distance = self.calculate_distances(individual)
            fitness = 1 / (current_distance + 1e-6)
            population_fitness.append(fitness)
        return np.array(population_fitness)

    def roulette_wheel_selection(self, population, fitness):
        total_fitness = np.sum(fitness)
        probabilities = fitness / total_fitness
        cumulative_prob = np.cumsum(probabilities)
        random_value = rand.random()
        for i, prob in enumerate(cumulative_prob):
            if random_value >= prob:
                return population[i]
        return population[0]

    def mutation(self, individual):
        if rand.random() <= self.mutation_rate:
            first, second = sorted(rand.sample(range(len(individual)), 2))
            individual[first], individual[second] = individual[second], individual[first]
        return individual

    def crossover(self, parent1, parent2):
        if rand.random() > self.crossover_rate:
            return parent2.copy()
        size = len(parent1)
        start, end = sorted(rand.sample(range(size), 2))
        child = [-1] * size
        child[start:end+1] = parent1[start:end+1]
        ptr = 0
        for chromosomes in parent2:
            if chromosomes not in child:
                while child[ptr] != -1:
                    ptr += 1
                child[ptr] = chromosomes
        return child

    def generation(self, population):
        new_population = []
        fitness = self.fitness(population)
        for _ in range(self.population):
            parent1 = self.roulette_wheel_selection(population, fitness)
            parent2 = self.roulette_wheel_selection(population, fitness)

            child = self.crossover(parent1, parent2)
            child = self.mutation(child)
            new_population.append(child)

        return np.array(new_population)

    def run(self):
        min_dist = None
        population = self.initialise()
        for generation in range(self.generations):
            population = self.generation(population)
            min_dist = min(population, key=self.calculate_distances)
        return min_dist


if __name__ == '__main__':
    cities = [0, 1, 2, 3, 4, 5]
    distance_map = np.array([
        [0.00, 38.02, 27.12, 33.46, 64.07, 42.1],
        [38.02, 0.00, 31.00, 29.55, 35.55, 38.4],
        [27.12, 31.00, 0.00, 28.03, 47.38, 57.9],
        [33.46, 29.55, 28.03, 0.00, 55.11, 20.07],
        [64.07, 35.55, 47.38, 55.11, 0.00, 16.02],
        [42.1, 38.4, 57.9, 20.07, 16.02, 0.00]
    ])

    ga = GeneticAlgorithm(
        population=20,
        generations=30,
        cities=cities,
        distance_map=distance_map,
        crossover_rate=0.9,
        mutation_rate=0.1
    )

    best = ga.run()
    print("Best Path Found:", best)
    print("Best Distance:", ga.calculate_distances(best))