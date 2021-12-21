import sp_crossover, mutator
import random

class Breeder:
    
    def __init__(self, crossover = sp_crossover.Crossover, mutation = mutator.Mutation):
        self.crossover = crossover
        self.mutation = mutation
        
    def produce_offspring(self, parents):
        offspring = []
        number_of_parents = len(parents)
        
        for index in range(int(number_of_parents / 2)):
            p1, p2 = self.__pick_random_parents(parents, number_of_parents)
            c1, c2 = self.crossover.crossover(p1, p2)
            c1m = self.mutation.mutate(c1)
            c2m = self.mutation.mutate(c2)
            offspring.extend((c1m, c2m))
            
        return offspring
            
    def __pick_random_parents(self, parents, number_of_parents: int):
        p1 = parents[random.randint(0, number_of_parents - 1)]
        p2 = parents[random.randint(0, number_of_parents - 1)]
        
        return p1, p2