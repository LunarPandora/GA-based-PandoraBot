from population import Population

MAX_GENERATION = 10
CHR_LTH = 2
MIN_LIMIT = -9
MAX_LIMIT = 9

for gen in range(MAX_GENERATION):
    generation = Population(6, MIN_LIMIT, MAX_LIMIT)
    
    chro = generation.population(CHR_LTH)
    fx_func = generation.fx(chro)
    fit = generation.fitness(chro, fx_func)
    fitness_chro = generation.fittest_chro(fit, 2)
    cr = generation.crossover(fitness_chro)
    
    print(cr)
    # cr1 = generation.crossover(fitness_chro, 1, 2)

    # mt = generation.mutation(cr1)
    # print(mt)
    # print(cr1)

# print(heritage[0].fittest)
# print(heritage[1].fittest)