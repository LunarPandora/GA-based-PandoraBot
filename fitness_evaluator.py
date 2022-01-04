import genotype_decoder

class FitnessEvaluator:
    
    def __init__(self, keyword: str):
        self.keyword = keyword
        
    def match(self, individuals):
        fitness = 0
        
        for x in range(len(self.keyword)):
            if(self.keyword[x] == individuals[x].char):
                fitness += 1
                
        return fitness
