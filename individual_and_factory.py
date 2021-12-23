import fitness_evaluator
import random

class Individual:
    
    def __init__(self, genotype: str, fitness: int):
        self.genotype = genotype
        self.fitness = fitness
        
    def __repr__(self):
        return "Individual/genotype = " + self.genotype + " Fitness = " + str(self.fitness)
    
class IndividualFactory:
    
    def __init__(self, genotype_length: int, fitness_evaluator: fitness_evaluator):
        self.genotype_length = genotype_length
        self.fitness_evaluator = fitness_evaluator
        
        self.binary_string_format = '{:0' + str(self.genotype_length) + 'b}'
        
    def with_random_genotype(self):
        genotype_max_value = self.genotype_length
        random_genotype = self.binary_string_format.format(random.randint(0, genotype_max_value))
        fitness = self.fitness_evaluator.evaluate(random_genotype)
        
        return Individual(random_genotype, fitness)
    
    def with_set_genotype(self, genotype: str):
        fitness = self.fitness_evaluator.evaluate(genotype)
        
        return Individual(genotype, fitness)
    
    def with_minimal_fitness(self):
        minimal_fitness_genotype = self.binary_string_format.format(0)
        fitness = self.fitness_evaluator.evaluate(minimal_fitness_genotype)
        
        return Individual(minimal_fitness_genotype, fitness)
    