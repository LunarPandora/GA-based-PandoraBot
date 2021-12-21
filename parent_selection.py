import population_and_factory
import random

class ParentSelector:
    
    def select_parents(self, population: population_and_factory.Population):
        total_fitness = 0
        fitness_scale = []
        
        for index, individual in enumerate(population.individuals):
            total_fitness += individual.fitness
            
            if index == 0:
                fitness_scale.append(individual.fitness)
            else:
                fitness_scale.append(individual.fitness + fitness_scale[index - 1])
                
        mating_pool = []
        number_of_parents = len(population.individuals)
        fitness_step = total_fitness / number_of_parents
        random_offset = random.uniform(0, fitness_step)
        
        current_fitness_pointer = random_offset
        last_fitness_scale_position = 0
        for index in range(len(population.individuals)):
            for fitness_scale_position in range(last_fitness_scale_position, len(fitness_scale)):
                if fitness_scale[fitness_scale_position] >= current_fitness_pointer:
                    mating_pool.append(population.individuals[fitness_scale_position])
                    last_fitness_scale_position = fitness_scale_position
                    
                    break
            
            current_fitness_pointer += fitness_scale_position
            
        return mating_pool