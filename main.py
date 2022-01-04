import fitness_evaluator, genotype_decoder, individual_and_factory, population_and_factory, sp_crossover, mutator, breeder, parent_selection, environment

target = "Hello"

TOTAL_GENERATIONS = 10000
POPULATION_SIZE = len(target)
GENOTYPE_LENGTH = 7

current_generation = 1

gen_dec = genotype_decoder.GenotypeDecoder()
fit_ev = fitness_evaluator.FitnessEvaluator(target)
individual_factory = individual_and_factory.IndividualFactory(GENOTYPE_LENGTH, gen_dec)
population_factory = population_and_factory.PopulationFactory(individual_factory, fit_ev)

cr = sp_crossover.Crossover(individual_factory)
mt = mutator.Mutation(individual_factory)
br = breeder.Breeder(cr, mt)
ps = parent_selection.ParentSelector()
env = environment.Environment(POPULATION_SIZE, ps, population_factory, br)

print(env.get_the_fittest())

highest_fitness_list = []

# while current_generation <= TOTAL_GENERATIONS:
#     fittest = env.get_the_fittest(1)[0]
    
#     if "0" not in fittest.genotype:
#         print("Finished!")
#         break
    
#     env.update()
#     current_generation += 1
    
# print("Stopped at generation " + str(current_generation - 1) + ". The fittest individual: ")
# print(fittest)

# print(env.get_the_fittest(1)[0])