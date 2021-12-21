import individual_and_factory
import random

class Crossover:
    
    def __init__(self, individual_factory: individual_and_factory.IndividualFactory):
        self.individual_factory = individual_factory
        
    def crossover(self, p1: individual_and_factory.Individual, p2: individual_and_factory.Individual):
        crossover_point = random.randint(0, len(p1.genotype))
        
        g1 = self.__new_genotype(crossover_point, p1, p2)
        g2 = self.__new_genotype(crossover_point, p2, p1)
        
        c1 = self.individual_factory.with_set_genotype(genotype = g1)
        c2 = self.individual_factory.with_set_genotype(genotype = g2)
        
        return c1, c2
        
    def __new_genotype(self, crossover_point: int, p1: individual_and_factory.Individual, p2: individual_and_factory.Individual):
        return p1.genotype[:crossover_point] + p2.genotype[crossover_point:]