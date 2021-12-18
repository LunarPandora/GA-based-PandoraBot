from population import Population

heritage = [Population(5), Population(5)]

for i in range(len(heritage)):
    heritage[i].population()
    heritage[i].bin2Dec()
    heritage[i].fitness()
    heritage[i].fittest_chro()

print(heritage[0].fittest)
print(heritage[1].fittest)