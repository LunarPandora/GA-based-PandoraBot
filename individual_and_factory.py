import fitness_evaluator, genotype_decoder
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
        genotype_max_value = 2 ** self.genotype_length
        random_genotype = self.binary_string_format.format(random.randint(0, genotype_max_value))
        fitness = self.fitness_evaluator.evaluate(random_genotype)
        
        return Individual(random_genotype, fitness)
    
    def with_set_genotype(self, genotype: str):
        # """
        # Evaluate given genotype and return an Individual instance.
        
        # @param   genotype: Genotype to evaluate.
        # @return  Individual
        # """

        fitness = self.fitness_evaluator.evaluate(genotype)
        
        return Individual(genotype, fitness)
    
    def with_minimal_fitness(self):
        # """
        # Create a genotype with minimal fitness point and return it as Individual instance.
        
        # @return  Individual
        # """
        
        minimal_fitness_genotype = self.binary_string_format.format(0)
        fitness = self.fitness_evaluator.evaluate(minimal_fitness_genotype)
        
        return Individual(minimal_fitness_genotype, fitness)
    
gen_dec = genotype_decoder.GenotypeDecoder()
fit_ev = fitness_evaluator.FitnessEvaluator(gen_dec)

a = IndividualFactory(7, fit_ev)                                                                                                                                                                                                                                                                                      

print(a.with_random_genotype())