import individual_and_factory, fitness_evaluator
import random

class Population:
    
    def __init__(self, individuals, fitness_evaluator: fitness_evaluator):
        self.individuals = individuals
        self.fitness_evaluator = fitness_evaluator
        
    def get_fitness(self):
        fv = self.fitness_evaluator
        fitness = fv.match(self.individuals)
        
        return fitness
        
    # def get_the_fittest(self, n: int):
    #     self.__sort_by_fitness()
        
    #     return self.individuals[:n]
    
    # def __sort_by_fitness(self):
    #     self.individuals.sort(key = self.__individual_fitness_sort_key, reverse = True)
        
    # def __individual_fitness_sort_key(self, individual: individual_and_factory.Individual):
    #     return individual.fitness
    
class PopulationFactory:
    
    def __init__(self, individual_factory: individual_and_factory.IndividualFactory, fitness_evaluator: fitness_evaluator):
        self.individual_factory = individual_factory
        self.fitness_evaluator = fitness_evaluator
        
    def with_random_individuals(self, size: int):
        individuals = []
        
        for i in range(size):
            individuals.append(self.individual_factory.with_random_genotype())
        
        return Population(individuals, self.fitness_evaluator)
    
    def with_individuals(self, individuals):
        return Population(individuals, self.fitness_evaluator)
    
    def with_minimal_fitness_individuals(self, size: int):
        individuals = []
        for i in range(size):
            individuals.append(self.individual_factory.with_minimal_fitness())
            
        return Population(individuals)