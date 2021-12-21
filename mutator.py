import individual_and_factory
import random

class Mutation:
    
    def __init__(self, individual_factory: individual_and_factory.IndividualFactory):
        self.individual_factory = individual_factory
        
    def mutate(self, individual: individual_and_factory.Individual):
        mutated_genotype = list(individual.genotype)
        mutation_probability = 1 / len(individual.genotype)
        
        for index, gene in enumerate(individual.genotype):
            if random.random() < mutation_probability:
                mutated_genotype[index] = '0' if gene == '1' else '1'
                
        return self.individual_factory.with_set_genotype(genotype = "".join(mutated_genotype))