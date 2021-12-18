import random

class Population:
    def __init__(self, num):
        self.num = num
        self.chro = []
        self.dec_chro = []
        self.test = []
        self.avg = 0
        self.fit = []
        self.sum_fit = 0
        
        self.fittest = []
        
    def generateChromosome(self, length):
        chromosome = ""

        for i in range(length):
            chromosome += str(int(round(random.random(), 0)))
            
        return chromosome
    
    def population(self):
        for i in range(self.num):
            # print(self.generateChromosome(20))
            self.chro.append(self.generateChromosome(20))
            
    def bin2Dec(self):
        for x in range(self.num):
            self.dec_chro.append(int(self.chro[x], 2))
            
    def fitness(self):
        for x in range(self.num):
            i = self.dec_chro[x]
            
            fx = ((i / 25) + 15) * 3
            self.test.append(fx)
            self.avg += fx
        
        self.avg = self.avg / self.num
        
        for y in range(self.num):
            res = round(10000 / self.test[y], 4)
            
            self.fit.append([self.chro[y], res])
            self.sum_fit += res
            
    def fittest_chro(self):
        arr_fit = []
        for i in range(self.num):
            arr_fit.append(self.fit[i][1])
            
        arr_fit.sort(reverse=True)
        for x in range(2):
            for y in range(self.num):
                if(arr_fit[x] == self.fit[y][1]):
                    self.fittest.append(self.fit[y][0])                    
            
    def crossover(self):
        x = random.randrange(1, 19)
        
        x1 = self.fittest[0][:x]
        x2 = self.fittest[1][x:]
        
        result = x1 + x2
        print(result)