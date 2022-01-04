import genotype_decoder
import random

class Individual: 
        
    def __init__(self, genotype: str, char: str):
        self.genotype = genotype
        self.char = char
        
    def __repr__(self):
        return "Individual/genotype = " + self.genotype + " Char = " + self.char
    
class IndividualFactory:
    
    def __init__(self, genotype_length: int, genotype_decoder: genotype_decoder.GenotypeDecoder):
        self.genotype_length = genotype_length
        self.genotype_decoder = genotype_decoder
        
        # self.binary_string_format = '{:0' + str(self.genotype_length) + 'b}'
    
    def rand_key(self, p):
        key = ""
 
        for i in range(p):
            temp = str(random.randint(0, 1))
            key += temp
         
        return key
    
    def with_random_genotype(self):
        genotype_max_value = self.genotype_length
        random_genotype = self.rand_key(genotype_max_value)
        char = self.genotype_decoder.decode(random_genotype)
        
        return Individual(random_genotype, char)
    
    # def with_set_genotype(self, genotype: str):
    #     # """
    #     # Evaluate given genotype and return an Individual instance.
        
    #     # @param   genotype: Genotype to evaluate.
    #     # @return  Individual
    #     # """

    #     fitness = self.fitness_evaluator.evaluate(genotype)
        
    #     return Individual(genotype, fitness)
    
    # def with_minimal_fitness(self):
    #     # """
    #     # Create a genotype with minimal fitness point and return it as Individual instance.
        
    #     # @return  Individual
    #     # """
        
    #     minimal_fitness_genotype = self.binary_string_format.format(0)
    #     fitness = self.fitness_evaluator.evaluate(minimal_fitness_genotype)
        
    #     return Individual(minimal_fitness_genotype, fitness)