import genotype_decoder

class FitnessEvaluator:
    
    def __init__(self, genotype_decoder: genotype_decoder):
        self.genotype_decoder = genotype_decoder
        
    def evaluate(self, genotype: str):
        return self.genotype_decoder.decode(genotype)
