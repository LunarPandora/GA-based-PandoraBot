class GenotypeDecoder:
    
    def decode(self, genotype: str):
        return int(genotype, 2) ** 2