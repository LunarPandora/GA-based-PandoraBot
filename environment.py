import parent_selection, population_and_factory, breeder

class Environment:
    
    def __init__(self,
                 population_size: int, 
                 parent_selector: parent_selection.ParentSelector,
                 population_factory: population_and_factory.PopulationFactory,
                 breeder: breeder.Breeder):
    
        self.population_factory = population_factory
        self.population = self.population_factory.with_random_individuals(size = population_size)
        self.parent_selector = parent_selector
        self.breeder = breeder
        
    def update(self):
        parents = self.parent_selector.select_parents(self.population)
        next_generation = self.breeder.produce_offspring(parents)
        self.population = self.population_factory.with_individuals(next_generation)
        
    def get_the_fittest(self, n: int):
        return self.population.get_the_fittest(n)